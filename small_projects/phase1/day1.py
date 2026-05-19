# create a numpy array of 50 randomly generated scores (0–100)
# find mean, median, highest, lowest score
# find students who scored below 40 (fail) and above 85 (distinction)
# normalize the scores between 0 and 1
# reshape the array into 5 rows × 10 students and compute row-wise averages
# add weightage (40% theory, 60% practical) and compute weighted final scores

import numpy as np

scores = np.random.randint(0, 100, size=50)

print("scores:\n", scores)

print("mean:", np.mean(scores))
print("median:", np.median(scores))
print("highest:", np.max(scores))
print("lowest:", np.min(scores))

fail_students = scores[scores < 40]
distinction_students = scores[scores > 85]

print("fail students:", fail_students)
print("distinction students:", distinction_students)

normalized_scores = (scores - np.min(scores)) / (np.max(scores) - np.min(scores))

print("normalized scores:\n", normalized_scores)

reshaped_scores = scores.reshape(5, 10)

print("reshaped scores:\n", reshaped_scores)

row_avg = np.mean(reshaped_scores, axis=1)

print("row wise averages:", row_avg)

theory = np.random.randint(0, 100, size=50)
practical = np.random.randint(0, 100, size=50)

final_scores = (0.4 * theory) + (0.6 * practical)

print("weighted final scores:\n", final_scores)