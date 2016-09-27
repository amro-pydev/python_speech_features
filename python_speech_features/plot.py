# Module for plotting wave files and MFCC parameters

import matplotlib.pyplot as plt
import numpy as np


def plot_mono_signal(signal,fs=8000,plot_title="Audio"):
    """ Function plots a mono signal.

    :param signal: mono channel signal
    :param fs: Sampling frequency for audio
    :param plot_title: Plot window title
    :return: None
    """
    # Generate the X-Axis
    x=np.linspace(0, len(signal)/fs, num=len(signal))

    # plot the first 1024 samples
    plt.plot(x,signal)

    # label the axes
    plt.ylabel("Amplitude")
    plt.xlabel("Time (Seconds)")

    # set the title
    plt.title(plot_title)

    # grid
    plt.grid()

    # display the plot
    plt.show()


def plot_mfcc(mfcc_feat,winstep=0.01,plot_title="MFCC"):
    """ This function plots a mono signal.

    :param mfcc_feat: MFCC features numpy array
    :param winstep: the step between successive windows in seconds. Default is 0.01s (10 milliseconds)
    :param plot_title: Plot window title
    :return: None
    """
    # Generate the mesh
    #xi, yi = np.linspace(0.0, mfcc_feat.shape[0] * winstep, mfcc_feat.shape[0]), np.linspace(0, mfcc_feat.shape[1], 1.0)
    #xi, yi = np.meshgrid(xi, yi)

    # plot the first 1024 samples
    #im = ax.imshow(zi, vmin=z.min(), vmax=z.max(), origin='lower',
    #           extent=[x.min(), x.max(), y.min(), y.max()], aspect='auto')

        #fig.colorbar(im, cax=ax, format=eng_formatter_second)
    plt.imshow(mfcc_feat.T,aspect=20.0)

    # label the axes
    plt.ylabel("Cep Parameters")
    plt.xlabel("Time (Seconds)")

    # set the title
    plt.title(plot_title)

    # Change Axis
    ax = plt.gca()
    ax.set_xticklabels(np.linspace(0.0, mfcc_feat.shape[0] * winstep, mfcc_feat.shape[0]))

    # display the plot
    plt.show()