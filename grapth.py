import os
import logging
import matplotlib.pyplot as plt
import json

logger = logging.getLogger()
logger.setLevel("INFO")


def visualize_statistics(data_file: str, path_to_file: str) -> None:
    """
    Функция создает график по данным
    :data_file: данные для построения
    :return: None
    """
    with open(data_file, "r") as f:
        data = json.load(f)
    averages = {}
    for key, values in data.items():
        average_value = sum(values) / len(values)
        averages[key] = average_value
    keys = list(averages.keys())
    values = list(averages.values())
    sorted_indices = sorted(range(len(keys)), key=lambda i: int(keys[i]))
    sorted_keys = [keys[i] for i in sorted_indices]
    sorted_values = [values[i] for i in sorted_indices]
    plt.figure(figsize=(12, 12))
    plt.plot(sorted_keys, sorted_values, marker="o",
             linestyle="-", color="green")
    plt.title("Size versus time graph")
    plt.xlabel("Size")
    plt.ylabel("Time, s")
    plt.grid(True)
    plt.savefig(os.path.join(path_to_file, "statistics.png"))
    logging.info("Schedule saved")