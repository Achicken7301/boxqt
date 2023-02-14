import pandas as pd
import time
from sklearn.preprocessing import StandardScaler


ax_window = []
ay_window = []
az_window = []
gx_window = []
gy_window = []
gz_window = []
window_mask = [ax_window, ay_window, az_window, gx_window, gy_window, gz_window]

count = 0
p_value = 0
total_p_value = []
total_p_value.append(0)

class Punch:
    def __init__(self) -> None:
        self.is_punched = False

    def setPunch(self, value: bool):
        self.is_punched = value
        return self.is_punched

    def getPunch(self):
        return self.is_punched


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
        "D:\laragon\www/boxqt\CNN/regression_model"
    )


def process_raw_data(queue):
    global count, p_value
    regresstion_input = pd.DataFrame()
    classified_input = pd.DataFrame()
    # get 10 data 1st
    window_size = 10
    # print("SLEEPT 500ms")
    while len(queue[0]) == 0:
        # print(queue[0])
        print("Wait for 1s")
        time.sleep(1)

    for _ in range(window_size):
        for j in range(6):
            window_mask[j].append(float(queue[j].pop(0)))

    while 1:
        global regresstion_model, classified_model, process_raw_data_flag
        if len(queue[0]) < 20:
            # Cancel process

            # print("Length queue < 20 samples ---> Sleep for 10ms")
            time.sleep(0.01)

            # POP EVERY DATA IN QUEUE
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
            # print(len(queue[0]))

            # Import data to window
            for _ in range(window_size):
                for j in range(6):
                    window_mask[j].append(float(queue[j].pop(0)))
            # """
            # process data time cost: 8ms
            # """
            process_window_data(
                regresstion_input,
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
            !!! WARNING: increase memory when put data in the model. DONT KNOW HOW TO FIX
            """
            global punch
            lowest_acel = 10
            if regresstion_input["a_mean"][0] > lowest_acel:
                for i in range(len(window_mask)):
                    classified_input[i] = window_mask[i]

                X_scaled = StandardScaler().fit_transform(classified_input)
                X_test = X_scaled.reshape(1, 20, 6, 1)

                [[np, p]] = classified_model.predict(X_test)

                if p > np:
                    # count += 1
                    # print(count)
                    print(classified_input)
                    # print(regresstion_input)
                    count += 1
                    [[p_value]] = regresstion_model.predict(regresstion_input)
                    total_p_value.append(p_value)
                    
                    # # Import data to window
                    # for _ in range(window_size):
                    #     for j in range(6):
                    #         window_mask[j].append(float(queue[j].pop(0)))

                    # # POP 10
                    # for window_index in range(6):
                    #     for _ in range(window_size):
                    #         window_mask[window_index].pop(0)

            # POP 10
            for window_index in range(6):
                for _ in range(window_size):
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
