from Device import Device


def main():

    # login
    # check in db login credentials
    # choose wich agent to run analytics or create new profile(new agent)
    # create Session for the chosen agent
    # perform analytics
    # display result
    ## store in db

    # ....skiping first 3 steps
    # device chosen somehow:
    device = Device('Device-01', '192.168.0.106', ('MD5User','MD5UserPass'), ('MD5DESUser', 'MD5DESUserPass'))

    device.createSession()
    # prob gonna change this function to return a tuple wich will feed some graphical engine
    device.performAnalytics()


if __name__ == '__main__':
    main()
