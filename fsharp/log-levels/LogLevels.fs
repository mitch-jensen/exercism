module LogLevels

let message (logLine: string): string =
    let index = logLine.IndexOf(" ")
    logLine.Substring(index).Trim()

let logLevel(logLine: string): string =
    let index = logLine.IndexOf(" ")
    logLine.Substring(0, index).Trim().Replace("[", "").Replace("]", "").Replace(":", "").ToLower()

let reformat(logLine: string): string =
    $"{message logLine} ({logLevel logLine})"
