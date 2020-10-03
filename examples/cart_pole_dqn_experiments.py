import logging
import numpy as np
import math
from examples import run_dqn_experiments


def run_experiment_with_result_files(folder,
                                     n_experiments,
                                     n_episodes,
                                     visualize,
                                     m_cart,
                                     m_pole,
                                     theta_0,
                                     theta_dot_0,
                                     time_step,
                                     positive_reward,
                                     negative_reward,
                                     force,
                                     log_level,
                                     binning,
                                     mode):
    """
    Runs experiments with the given configuration and writes episodes length of all experiment as one file
    and execution times of experiments as another.
    File names are composed from numerical experiment parameters
    in the same order as in function definition.
    Episodes length are written as 2d-array of shape (n_episodes, n_experiments):
    i-th row - i-th episode, j-th column - j-th experiment.

    Execution times are written as 1d-array of shape (n_experiments, ): j-th element - j-th experiment


    :param folder: folder for experiment result files
    :return: None
    """
    experiment_file_name_prefix = "{}/experiment_{}_{}_{}_{}_{:.0f}_{}_{}_{}_{}_{}_{}_{}_".format(
        folder,
        n_experiments,
        n_episodes,
        m_cart,
        m_pole,
        theta_0 * 180 / math.pi,
        theta_dot_0,
        time_step,
        positive_reward,
        negative_reward,
        force,
        binning,
        mode
    )
    _, episodes_lengths, exec_times = run_dqn_experiments(n_experiments=n_experiments,
                                                         n_episodes=n_episodes,
                                                         visualize=visualize,
                                                         m_cart=m_cart,
                                                         m_pole=m_pole,
                                                         theta_0=theta_0,
                                                         theta_dot_0=theta_dot_0,
                                                         time_step=time_step,
                                                         positive_reward=positive_reward,
                                                         negative_reward=negative_reward,
                                                         force=force,
                                                         log_level=log_level,
                                                          binning=binning,
                                                          mode=mode)

    np.savetxt(fname=experiment_file_name_prefix + "episodes_lengths.csv",
               X=np.transpose(episodes_lengths),
               delimiter=",",
               fmt="%d")
    np.savetxt(fname=experiment_file_name_prefix + "exec_times.csv",
               X=np.array(exec_times),
               delimiter=",",
               fmt="%.4f")


def binning_experiment(folder, mode="CS"):
    run_experiment_with_result_files(folder,
                                     n_experiments=5,
                                     n_episodes=100,
                                     visualize=False,
                                     m_cart=10,
                                     m_pole=1,
                                     theta_0=85 / 180 * math.pi,
                                     theta_dot_0=0,
                                     time_step=0.05,
                                     positive_reward=1,
                                     negative_reward=-100,
                                     force=11,
                                     log_level=logging.INFO,
                                     binning=True,
                                     mode=mode)
    run_experiment_with_result_files(folder,
                                     n_experiments=5,
                                     n_episodes=100,
                                     visualize=False,
                                     m_cart=10,
                                     m_pole=1,
                                     theta_0=85 / 180 * math.pi,
                                     theta_dot_0=0,
                                     time_step=0.05,
                                     positive_reward=1,
                                     negative_reward=-100,
                                     force=11,
                                     log_level=logging.INFO,
                                     binning=False,
                                     mode=mode)


if __name__ == "__main__":
    import time
    start = time.time()
    folder = "experiments_results/dqn"
    binning_experiment(folder, mode="ME")
    binning_experiment(folder, mode="CS")
    end = time.time()
    print("Total execution time {:.2f} seconds".format(end-start))
