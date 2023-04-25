import pandas as pd
import time
from sklearn.preprocessing import StandardScaler

# import models
from models.PunchModel import Punch

ax_window = []
ay_window = []
az_window = []
gx_window = []
gy_window = []
gz_window = []
window_mask = [ax_window, ay_window, az_window, gx_window, gy_window, gz_window]

count = 0
p_value = 0
total_p_value = list()
total_p_value.append(float(0))


punch = Punch()


def importCnnModel():
    import tensorflow as tf

    global classified_model, regresstion_model
    #  TODO SPEED THINGS UP
    # https://stackoverflow.com/questions/65298241/what-does-this-tensorflow-message-mean-any-side-effect-was-the-installation-su#:~:text=which%20can%20speed%20things%20up
    classified_model = tf.keras.models.load_model(
        "D:\laragon\www/boxqt\CNN\classified_model"
    )
    regresstion_model = tf.keras.models.load_model(
        "D:/laragon/www/boxqt/CNN/regression_model"
    )


def process_raw_data(queue):
    global count, p_value, acceleration_data_for_view, df1, regresstion_model, classified_model, process_raw_data_flag, count, raw_data
    acceleration_data_for_view = pd.DataFrame()
    df1 = pd.DataFrame()
    raw_data = pd.DataFrame()
    regresstion_input = pd.DataFrame()

    window_size = 10

    regg_flag = 0
    pre_p = pd.DataFrame()

    while len(queue[0]) == 0:
        # print(queue[0])
        print("Wait for 1s")
        time.sleep(1)
        if process_raw_data_flag:
            break

    queue_push(queue, 20 - window_size)
    while 1:
        if len(queue[0]) < 20:
            # Wait for data fill in queue
            time.sleep(0.01)

            # POP EVERY DATA IN QUEUE BEFORE CLOSE THREAD
            if process_raw_data_flag:

                # REMOVE EVERYTHING IN QUEUE
                while len(queue[0]) != 0:
                    for i in range(len(queue)):
                        queue[i].pop(0)

                # REMOVE EVERYTHING IN WINDOW_MASK
                while len(window_mask[0]) != 0:
                    for i in range(len(window_mask)):
                        window_mask[i].pop(0)

                break
        else:
            # Import data to window
            queue_push(queue, window_size)

            # process data time cost: 8ms
            process_window_data(
                regresstion_input,
                window_mask[0],
                window_mask[1],
                window_mask[2],
                window_mask[3],
                window_mask[4],
                window_mask[5],
            )

            global punch
            lowest_acel_std = 2.5

            print(regresstion_input["a_std"][0])

            # Algorithm: more details in MY thesis
            if regg_flag == 1:
                if isOverThreshHold(regresstion_input, lowest_acel_std):
                    if pre_p["a_std"][0] > regresstion_input["a_std"][0]:
                        predict_window(pre_p)
                    else:
                        predict_window(regresstion_input)
                else:
                    predict_window(pre_p)

                regg_flag = 0
                queue_push(queue, window_size)

                # POP 10
                for window_index in range(6):
                    for _ in range(window_size):
                        window_mask[window_index].pop(0)

            else:
                if isOverThreshHold(regresstion_input, lowest_acel_std):
                    regg_flag = 1
                    pre_p = regresstion_input.copy()

                queue_push(queue, window_size)

                # POP 10
                for window_index in range(6):
                    for _ in range(window_size):
                        window_mask[window_index].pop(0)

            # POP 10
            for window_index in range(6):
                for _ in range(window_size):
                    window_mask[window_index].pop(0)


def predict_window(regresstion_input: pd.DataFrame):
    global count, total_p_value, df1, p_value, raw_data

    df1 = pd.concat(
        [df1, regresstion_input],
        axis=0,
    )
    count += 1

    predict_data = regresstion_input[["g_std"]].copy()

    # print(predict_data)

    (cols, rows) = (1, 1)

    predict_data = predict_data.values.reshape(1, cols, rows)

    [[p_value]] = regresstion_model.predict(predict_data)
    total_p_value.append(float(p_value))


def isOverThreshHold(regresstion_input, threshold):
    return regresstion_input["a_std"][0] > threshold


def queue_push(queue, window_size):
    for _ in range(window_size):
        for j in range(6):
            window_mask[j].append(float(queue[j].pop(0)))


def process_window_data(
    input: pd.DataFrame,
    ax_popped: list,
    ay_popped: list,
    az_popped: list,
    gx_popped: list,
    gy_popped: list,
    gz_popped: list,
):
    pd_ax_popped = pd.DataFrame(ax_popped)
    pd_ay_popped = pd.DataFrame(ay_popped)
    pd_az_popped = pd.DataFrame(az_popped)
    pd_gx_popped = pd.DataFrame(gx_popped)
    pd_gy_popped = pd.DataFrame(gy_popped)
    pd_gz_popped = pd.DataFrame(gz_popped)

    ax_std = pd_ax_popped.std()
    ay_std = pd_ay_popped.std()
    az_std = pd_az_popped.std()
    gx_std = pd_gx_popped.std()
    gy_std = pd_gy_popped.std()
    gz_std = pd_gz_popped.std()

    gx_max = pd_gx_popped.max()
    gy_max = pd_gy_popped.max()
    gz_max = pd_gz_popped.max()

    # input["a_mean"] = pow(pow(ax_mean, 2) + pow(ay_mean, 2) + pow(az_mean, 2), 1 / 2)
    # input["g_mean"] = pow(pow(gx_mean, 2) + pow(gy_mean, 2) + pow(gz_mean, 2), 1 / 2)
    input["a_std"] = pow(pow(ax_std, 2) + pow(ay_std, 2) + pow(az_std, 2), 1 / 2)
    input["g_std"] = pow(pow(gx_std, 2) + pow(gy_std, 2) + pow(gz_std, 2), 1 / 2)
    input["g_max"] = pow(pow(gx_max, 2) + pow(gy_max, 2) + pow(gz_max, 2), 1 / 2)
