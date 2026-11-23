from bemchmarker import run_benchmark
import demo_run
from test_registrations import testnow


if __name__ == "__main__":

    choice = input("Choose what to run: \n Demo run(d) \n ------------------ \n Benchmark run(b) \n ------------------ \n Scenario Tets(t) \n: ")

    if choice == "d":
        demo_run.demo_run()

    elif choice == "b":
        resfile = input("Please specify name for the results file: ")
        run_benchmark(resfile)

    elif choice == "t":
        testnow()


    else:
        print("Wrong input, please restart the program and choose option \"d\" or \"b\" or \"t\"")