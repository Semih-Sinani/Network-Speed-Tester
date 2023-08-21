import speedtest

st = speedtest.Speedtest()

while True:
    download_speed = st.download()

    