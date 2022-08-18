workflow Test-Workflow{
    python --version
    pwd
    pytest --browser firefox -n 10 --html=firefox-report.html
    # pytest --browser firefox -n 10 --html=firefox-report.html
    # ForEach ($browser in @('chrome', 'edge', 'firefox'))
    # {
    #     "Processing $browser"
    #     # pytest --browser $browser -n 10 --html=$browser-report.html
    # }
}
Test-Workflow