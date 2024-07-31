import threading
import time
import matplotlib.pyplot as plt

# Function that each thread will execute
def thread_task(thread_id, duration, start_times, end_times):
    start_times[thread_id] = time.time()
    time.sleep(duration)
    end_times[thread_id] = time.time()

def initialize_times(num_threads):
    start_times = [0] * num_threads
    end_times = [0] * num_threads
    return start_times, end_times

def start_threads(num_threads, durations, start_times, end_times):
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=thread_task, args=(i, durations[i], start_times, end_times))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

def plot_activity_chart(start_times, end_times):
    # Normalize times
    min_start_time = min(start_times)
    start_times = [start_time - min_start_time for start_time in start_times]
    end_times = [end_time - min_start_time for end_time in end_times]

    # Plot the activity chart
    fig, ax = plt.subplots()
    for i in range(len(start_times)):
        ax.plot([start_times[i], end_times[i]], [i, i], marker='o')

    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Thread ID')
    ax.set_title('Thread Activity Chart')
    plt.show()

if __name__ == "__main__":
    num_threads = 5
    durations = [1, 2, 1.5, 3, 2.5]  # Durations for each thread
    start_times, end_times = initialize_times(num_threads)
    start_threads(num_threads, durations, start_times, end_times)
    plot_activity_chart(start_times, end_times)
