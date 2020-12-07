$day = $args[0]
New-Item ".\Day_${day}a.py"
New-Item ".\Day_${day}b.py"
New-Item "input$day.csv"
New-Item "input${day}test.csv"