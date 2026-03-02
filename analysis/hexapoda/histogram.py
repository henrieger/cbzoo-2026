import matplotlib.pyplot as plt

with open("histogram.dat") as file:
    parsimony_scores: list[int] = [int(line.strip()) for line in file.readlines()]

parsimony_scores: list[int] = []
rearrangements: list[int] = []
generations: list[list[int]] = []
for i in range(1000):
    with open(f"hexapoda_{i:03}.dat") as file:
        score, rearr, *gen = [line.strip().split(".")[0] for line in file.readlines()]
        parsimony_scores.append(int(score))
        rearrangements.append(int(rearr))
        generations.append([int(g) for g in gen])

generations_max: int = max(len(g) for g in generations)
for run in generations:
    run += [run[-1]] * (generations_max - len(run))
avg_generation: list[float] = [sum(run) / len(run) for run in zip(*generations)]

nbins: int = max(parsimony_scores) - min(parsimony_scores) + 1
plt.subplot(2, 2, 1)
plt.hist(parsimony_scores, bins=nbins, color="#32b351")
plt.title("Length distribution")

plt.subplot(2, 2, 2)
plt.hist(rearrangements, color="#32b351")
plt.title("Rearrangements distribution")

plt.subplot(2, 1, 2)
plt.yscale("log")
for run in generations:
    plt.plot(run, alpha=0.15, color="#aaaaaa")
plt.plot(avg_generation, alpha=1.0, color="#32b351")
plt.title("Scores per generation")

plt.suptitle("Hexapoda")
plt.subplots_adjust(hspace=0.4)
plt.savefig("histogram.pdf", format="pdf")
