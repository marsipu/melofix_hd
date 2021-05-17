import numpy as np


def melofix_event_handling(meeg):

    try:
        events = meeg.load_events()
    except FileNotFoundError:
        raise RuntimeError(f'No events found for {meeg.name}, "Find Events HD" has to be called first')

    # Event-ID assignment for Melody-Fixed-Paradigm
    for n in range(len(events)):
        if events[n, 2] == 58:

            # Fixed Paradigm
            if events[n - 1, 2] == events[n - 2, 2] == events[n - 3, 2] == events[n - 4, 2]:

                # Fixed-Onset = 1
                events[n - 4, 2] = 1
                # Fixed 2-4
                events[n - 3, 2] = 2
                events[n - 2, 2] = 2
                events[n - 1, 2] = 2
            else:
                # Melody-Onset = 3
                events[n - 4, 2] = 3
                # Melody 2-4
                events[n - 3, 2] = 4
                events[n - 2, 2] = 4
                events[n - 1, 2] = 4

    # unique event_ids
    ids = np.unique(events[:, 2])
    print('unique ID\'s assigned: ', ids)
    meeg.save_events(events)


def melofix_event_handling_updown(meeg):
    try:
        events = meeg.load_events()
    except FileNotFoundError:
        raise RuntimeError(f'No events found for {meeg.name}, "Find Events HD" has to be called first')

    # Event-ID assignment for Melody-Fixed-Paradigm with Melody Up/Down
    for n in range(len(events)):
        if events[n, 2] == 58:
            # Fixed Paradigm
            if events[n - 1, 2] == events[n - 2, 2] == events[n - 3, 2] == events[n - 4, 2]:

                # Fixed-Onset = 1
                events[n - 4, 2] = 1
                # Fixed 2
                events[n - 3, 2] = 2
                events[n - 2, 2] = 2
                events[n - 1, 2] = 2

            elif events[n - 1, 2] == 45:

                # Melody-Up Onset = 5
                events[n - 4, 2] = 5
                # Melody-Up Trans = 6
                events[n - 3, 2] = 6
                events[n - 2, 2] = 6
                events[n - 1, 2] = 6

            elif events[n - 1, 2] == 33:

                # Melody-Down Onset = 7
                events[n - 4, 2] = 7
                # Melody-Down Trans = 8
                events[n - 3, 2] = 8
                events[n - 2, 2] = 8
                events[n - 1, 2] = 8

    # unique event_ids
    ids = np.unique(events[:, 2])
    print('unique ID\'s assigned: ', ids)
    meeg.save_events(events)
