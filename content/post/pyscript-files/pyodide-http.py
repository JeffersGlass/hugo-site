def open_url(url: str) -> StringIO:
    """Fetches a given URL synchronously.
    The download of binary files is not supported. To download binary
    files use :`pyodide.http.pyfetch` which is asynchronous."""