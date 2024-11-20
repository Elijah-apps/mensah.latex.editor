import wx
import wx.html2

class HTMLViewer(wx.Frame):
    def __init__(self, parent, title):
        super(HTMLViewer, self).__init__(parent, title=title, size=(800, 600))

        # Create a WebView for displaying the HTML file
        self.browser = wx.html2.WebView.New(self)
        
        # Load the HTML file
        html_file_path = "index.html"  # Change this to the path of your HTML file
        self.browser.LoadURL(f'file:///{html_file_path}')
        
        self.Show(True)

def main():
    app = wx.App(False)
    HTMLViewer(None, title="Mensah Latex Editor")
    app.MainLoop()

if __name__ == "__main__":
    main()
