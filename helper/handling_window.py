class windowHandling:

    def __init__(self):
        self.driver = None

    def go_to_parent_window(self, index2):
        print(self.driver.current_window_handle)
        parent_window = self.driver.window_handles[index2]
        self.driver.switch_to.window(parent_window)

    def go_to_child_window(self, index1):
        print(self.driver.current_window_handle)
        child_window = self.driver.window_handles[index1]
        self.driver.switch_to.window(child_window)
