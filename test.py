# import time
#
# def print_help():
#     # Help message
#     print("This is a help message.")
#
# def main_process():
#     # Get the current time
#     start_time = time.time()
#
#     # Calculate the end time
#     end_time = start_time + 300  # 5 minutes = 300 seconds
#
#     while time.time() < end_time:
#         # Call the print_help function every 5 seconds
#         print_help()
#         time.sleep(5)  # Wait for 5 seconds
#
# # Start the main process
# main_process()


my_list = [10, 20, 630, 540, 50]
new_list = [100, 200, 300, 400, 500]

# Find the index of the maximum value
max_index = my_list.index(max(my_list))

print("Index of the maximum value:", max_index)
print("Index of the maximum value:", new_list[max_index])