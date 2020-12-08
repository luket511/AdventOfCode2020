$day = $args[0]
New-Item ".\Day_${day}a.py"
New-Item ".\Day_${day}b.py"
New-Item "input$day.csv"
New-Item "input${day}test.csv"

$template = @"
from commonFunctions import reader
INPUT = "input${day}test.csv"




if __name__ == "__main__":
    pass
"@

Write-Output $template > ".\Day_${day}a.py"
Write-Output $template > ".\Day_${day}b.py"