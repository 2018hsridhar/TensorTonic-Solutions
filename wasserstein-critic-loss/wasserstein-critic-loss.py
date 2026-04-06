import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss for WGAN.
    Real-valued score vs probability
    """
    # Write code here
    mean_real_scores = np.mean(real_scores)
    mean_fake_scores = np.mean(fake_scores)
    return -1 * (mean_real_scores - mean_fake_scores)
