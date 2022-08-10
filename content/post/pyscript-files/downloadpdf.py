from js import window

url = window.URL.createObjectURL(file_object)

hidden_link = document.createElement("a")
hidden_link.download = 'document.pdf'
hidden_link.href = url
print(f"Created hiddden link with url {hidden_link.href}")