#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#define N 1000
#define UL static unsigned long
#define KATA unsigned int

double timeval_diff(struct timeval *start, struct timeval *end) {
    double diff_sec = end->tv_sec - start->tv_sec;
    double diff_usec = end->tv_usec - start->tv_usec;
    return diff_sec + diff_usec / 1e6;
}

int main(void) {
  int i, j, k;

  struct timeval tv_start, tv_end;
  struct timespec ts_start, ts_end;
  
  UL a[N][N] = {{0}};
  UL b[N][N] = {{0}};
  UL c[N][N] = {{0}};

  for(i = 0; i < N; i++) {
    for(j = 0; j < N; j++) {
      a[i][j] = (rand() % 10);
      b[i][j] = (rand() % 10);
      c[i][j] = 0;
    }
  }

  // gettimeofday()を使用した処理時間計測
  gettimeofday(&tv_start, NULL);
  for(i = 0; i < N; i++) {
    for(j = 0; j < N; j++) {
      for (k = 0; k < N; k++){
	c[i][j] += a[i][k] * b[k][j];
      }
    }
  }
  gettimeofday(&tv_end, NULL);
  double elapsed_time_tv = timeval_diff(&tv_start, &tv_end);
  printf("gettimeofday() elapsed time: %f seconds\n", elapsed_time_tv);


  
  for(i = 0; i < N; i++) {
    for(j = 0; j < N; j++) {
      a[i][j] = (rand() % 10);
      b[i][j] = (rand() % 10);
      c[i][j] = 0;
    }
  }

  

  // clock_gettime()を使用した処理時間計測
  clock_gettime(CLOCK_MONOTONIC, &ts_start);
  for(i = 0; i < N; i++) {
    for(j = 0; j < N; j++) {
      for (k = 0; k < N; k++){
	c[i][j] += a[i][k] * b[k][j];
      }
    }
  }
  clock_gettime(CLOCK_MONOTONIC, &ts_end);
  double elapsed_time_ts = ts_end.tv_sec - ts_start.tv_sec +
    (ts_end.tv_nsec - ts_start.tv_nsec) / 1e9;
  printf("clock_gettime() elapsed time: %f seconds\n", elapsed_time_ts);

    
  return 0;
}
  
