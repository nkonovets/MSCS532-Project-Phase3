from bemchmarker import run_benchmark
import demo_run


if __name__ == "__main__":

    choice = input("Choose what to run: \n Demo run(d) \n ------------------ \n Benchmark run(b) \n: ")

    if choice == "d":
        demo_run.main()

    elif choice == "b":
        version = input("Please specify name for the results file: ")
        run_benchmark(version)

    else:
        print("Wrong input, please restart the program and choose option \"d\" or \"b\" ")