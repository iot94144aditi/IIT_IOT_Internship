prices = [105, 110, 108, 112, 115, 116, 114]
rolling_averages = []
window_size = 3

for i in range(window_size - 1, len(prices)):
    window = prices[i - window_size + 1 : i + 1]
    average = sum(window) / len(window)
    rolling_averages.append(round(average, 2))

print(rolling_averages)
 
