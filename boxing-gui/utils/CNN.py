import pandas as pd
import time

global count
count = 0

input = pd.DataFrame()

ax_window = []
ay_window = []
az_window = []
gx_window = []
gy_window = []
gz_window = []
window_mask = [ax_window, ay_window, az_window, gx_window, gy_window, gz_window]


def importCnnModel():
    import tensorflow as tf

    global reloaded_model
    #  TODO SPEED THINGS UP
    # https://stackoverflow.com/questions/65298241/what-does-this-tensorflow-message-mean-any-side-effect-was-the-installation-su#:~:text=which%20can%20speed%20things%20up
    reloaded_model = tf.keras.models.load_model("D:/laragon/www/boxqt/CNN/model")


def process_raw_data(queue):
    # get 10 data 1st
    time.sleep(0.5)
    for _ in range(10):
        for j in range(6):
            window_mask[j].append(float(queue[j].pop(0)))

    while 1:
        if len(queue[0]) < 20:
            global process_raw_data_flag
            # Cancel process
            if process_raw_data_flag:
                break

            # print("Length queue < 20 samples ---> Sleep for 10ms")
            time.sleep(0.01)
        else:
            global reloaded_model

            # Import data to window
            for _ in range(10):
                for j in range(6):
                    window_mask[j].append(float(queue[j].pop(0)))
            """
            process data time cost: 8ms
            """
            process_window_data(
                input,
                window_mask[0],
                window_mask[1],
                window_mask[2],
                window_mask[3],
                window_mask[4],
                window_mask[5],
            )
            """
            import data to window CNN and output force
            with condition a_mean TODO may change the condition for better performance
            lowest_acel is a aceleration value when no punch
            WARNING: increase memory when put data in the model.
            """
            lowest_acel = 10
            if input["a_mean"][0] > lowest_acel:
                force = reloaded_model.predict(input)
                print("Force predict: " + str(force[0]))

            for window_index in range(6):
                for _ in range(10):
                    window_mask[window_index].pop(0)


def process_window_data(
    input: pd.DataFrame,
    ax_popped: list,
    ay_popped: list,
    az_popped: list,
    gx_popped: list,
    gy_popped: list,
    gz_popped: list,
):
    ax_popped = pd.DataFrame(ax_popped)
    ax_mean = ax_popped.abs().mean()
    ax_std = ax_popped.std()

    ay_popped = pd.DataFrame(ay_popped)
    ay_mean = ay_popped.abs().mean()
    ay_std = ay_popped.std()

    az_popped = pd.DataFrame(az_popped)
    az_mean = az_popped.abs().mean()
    az_std = az_popped.std()

    gx_popped = pd.DataFrame(gx_popped)
    gx_mean = gx_popped.abs().mean()
    gx_std = gx_popped.std()

    gy_popped = pd.DataFrame(gy_popped)
    gy_mean = gy_popped.abs().mean()
    gy_std = gy_popped.std()

    gz_popped = pd.DataFrame(gz_popped)
    gz_mean = gz_popped.abs().mean()
    gz_std = gz_popped.std()

    input["a_mean"] = pow(pow(ax_mean, 2) + pow(ay_mean, 2) + pow(az_mean, 2), 1 / 2)
    input["g_mean"] = pow(pow(gx_mean, 2) + pow(gy_mean, 2) + pow(gz_mean, 2), 1 / 2)
    input["a_std"] = pow(pow(ax_std, 2) + pow(ay_std, 2) + pow(az_std, 2), 1 / 2)
    input["g_std"] = pow(pow(gx_std, 2) + pow(gy_std, 2) + pow(gz_std, 2), 1 / 2)
