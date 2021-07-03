#include <stdio.h>
#include <thread>
#include <mutex>
#include <chrono>

using namespace std::chrono;

int count;
const int N = 20000;

std::mutex m;

void race_increment() {
    for (int i = 0; i < N; ++i)
        ++count;
}

void race_decrement() {
    for (int i = 0; i < N; ++i)
        ++count;
}

void no_race_increment() {
    m.lock();
    for (int i = 0; i < N; ++i)
        ++count;
    m.unlock();
}

void no_race_decrement() {
    m.lock();
    for (int i = 0; i < N; ++i)
        --count;
    m.unlock();
}

void run(void (*inc) (), void (*dec) ()) {
    count = 0;

    std::thread threads[] = {
        std::thread(inc),
        std::thread(dec),
        std::thread(inc),
        std::thread(dec)};

    for (int i = 0; i < 4; ++i) {
        threads[i].join();
    }
}

int main(int argc, char const* argv[]) {
    int n_iterations;

    if (argc >= 2) {
        n_iterations = atoi(argv[1]);
    } else {
        n_iterations = 10'000;
    }

    printf("race,no_race\n");

    for (int i = 0; i < n_iterations; ++i) {
        auto begin = steady_clock::now();
        run(&race_increment, &race_decrement);
        auto end = steady_clock::now();

        long race_time = duration_cast<microseconds>(end - begin).count();

        begin = steady_clock::now();
        run(&no_race_increment, &no_race_decrement);
        end = steady_clock::now();

        long no_race_time = duration_cast<microseconds>(end - begin).count();

        printf("%ld,%ld\n", race_time, no_race_time);
    }

    return 0;
}
