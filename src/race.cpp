#include <stdio.h>
#include <thread>

int count;
const int N = 20000;

void increment() {
    for (int i = 0; i < N; ++i)
        ++count;
}

void decrement() {
    for (int i = 0; i < N; ++i)
        --count;
}

void run_race_condition() {
    count = 0;

    std::thread threads[] = {
        std::thread(&increment),
        std::thread(&decrement),
        std::thread(&increment),
        std::thread(&decrement)
    };

    for (int i = 0; i < 4; ++i) {
        threads[i].join();
    }
}

int main(int argc, char const * argv []) {
    int n_iterations;

    if (argc >= 2) {
        n_iterations = atoi(argv[1]);
    }
    else {
        n_iterations = 200'000;
    }

    for (int i = 0; i < n_iterations; ++i) {
        run_race_condition();

        printf("%d\n", count);
    }

    return 0;
}
