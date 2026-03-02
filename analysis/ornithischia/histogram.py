import matplotlib.pyplot as plt
from os import stat

parsimony_scores: list[int] = []
rearrangements: list[int] = []
generations: list[list[int]] = []
for i in range(1000):
    if not stat(f"ornithischia_{i:03}.dat").st_size:
        continue
    with open(f"ornithischia_{i:03}.dat") as file:
        score, rearr, *gen = [line.strip().split(".")[0] for line in file.readlines()]
        parsimony_scores.append(int(score))
        rearrangements.append(int(rearr))
        generations.append([int(g) for g in gen])

generations_max: int = max(len(g) for g in generations)
for run in generations:
    run += [run[-1]] * (generations_max - len(run))
avg_generation: list[float] = [sum(run) / len(run) for run in zip(*generations)]

plt.subplot(2, 2, 1)
plt.hist(parsimony_scores, bins=30, color="#eb8021")
plt.title("Length distribution")

plt.subplot(2, 2, 2)
plt.hist(rearrangements, color="#eb8021")
plt.title("Rearrangements distribution")

plt.subplot(2, 1, 2)
plt.yscale("log")
for run in generations:
    plt.plot(run, alpha=0.15, color="#aaaaaa")
plt.plot(avg_generation, alpha=1.0, color="#eb8021")
plt.title("Scores per generation")

plt.suptitle("Ornithischia")
plt.subplots_adjust(hspace=0.4)
plt.savefig("histogram.pdf", format="pdf")
