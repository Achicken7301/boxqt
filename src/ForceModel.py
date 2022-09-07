class ForceModel(object):
    """docstring for ForceModel"""

    def __init__(self, arg):
        super(ForceModel, self).__init__()
        self.arg = arg

    def update_data_force_on_bag(self):
        length = 500

        self.x = list(range(length))
        self.force = [0 for _ in range(length)]
        self.force_graph.setBackground("w")

        # # Add legend (line name)
        self.force_graph.addLegend()

        # # Add Title
        self.force_graph.setTitle("Force Graph", color="b", size="10pt")

        width = 1
        pen_force_graph = pg.mkPen("r", width=width)

        self.data_line_force_graph = self.force_graph.plot(self.x,
                                                           self.force,
                                                           pen=pen_force_graph,
                                                           name="force")

        self.x = self.x[1:]  # Remove the first y element.
        # Add a new value 1 higher than the last.
        self.x.append(self.x[-1] + 1)
        b = self.ser.readline()
        # Cannot decode the 1st value b'\xb4j7\r\n'
        # solve this with try except
        try:
            string_n = b.decode()
            print(string_n)
            [force, a_x, a_y, a_z, g_x, g_y, g_z] = string_n.split()
            # Acceleration
            self.force = self.force[1:]
            self.force.append(float(force))
        except Exception as e:
            print(e)
        # Update the data.
        self.data_line_force_graph.setData(self.x, self.force)
