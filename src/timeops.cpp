#include <chrono>
#include <stdio.h>
#include <stdlib.h>

int count = 0;

const int N = 1000;

using namespace std::chrono;

void increment() {
    ++count;
}

void decrement() {
    --count;
}

double time(void (*func)()) {
    long elapsed_time = 0;

    for (int i = 0; i < N; ++i) {
        auto start = steady_clock::now();
        func();
        auto end = steady_clock::now();

        elapsed_time += duration_cast<nanoseconds>(end - start).count();
    }

    auto time_per_op = (double) elapsed_time / N;

    return time_per_op;
}

int main(int argc, char const* argv[]) {
    int n_iterations;

    if (argc >= 2) {
        n_iterations = atoi(argv[1]);
    }
    else {
        n_iterations = 10'000;
    }

    printf("increment,decrement\n");
    for (int i = 0; i < n_iterations; ++i) {
        double inc_time = time(increment);
        double dec_time = time(decrement);
        printf("%lf,%lf\n", inc_time, dec_time);
    }

    return 0;
}
