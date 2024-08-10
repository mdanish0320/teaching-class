import time
import matplotlib.pyplot as plt

def initialize_times(num_threads):
    start_times = [0] * num_threads
    end_times = [0] * num_threads
    return start_times, end_times

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




def task(num_of_run, start_times, end_times):
    start_times[num_of_run] = time.time()
    time.sleep(2)
    end_times[num_of_run] = time.time()

if __name__ == "__main__":
    num_of_run = 5
    start_times, end_times = initialize_times(num_of_run)

    for i in range(num_of_run):
        task(i, start_times, end_times)

    plot_activity_chart(start_times, end_times)