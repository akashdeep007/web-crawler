import pygtk
pygtk.require('2.0')
import gtk, gobject


def progress_timeout(pbobj):
        pbobj.pbar.pulse()
        return True

class ProgressBar:
    # Callback that toggles the text display within the progress
    # bar trough
 
    def destroy_progress(self, widget, data=None):
        gobject.source_remove(self.timer)
        self.timer = 0
        gtk.main_quit()
            
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_resizable(True)
        self.window.set_size_request(500,100)

        self.window.connect("destroy", self.destroy_progress)
        self.window.set_title("ProgressBar")
        self.window.set_border_width(0)

        vbox = gtk.VBox(False, 5)
        vbox.set_border_width(10)
        self.window.add(vbox)
        vbox.show()
  
        # Create a centering alignment object
        align = gtk.Alignment(0.5, 0.5, 0, 0)
        vbox.pack_start(align, False, False, 5)
        align.show()

        # Create the ProgressBar
        self.pbar = gtk.ProgressBar()
        self.pbar.set_fraction(0.0)
        print self.pbar.get_fraction()
        align.add(self.pbar)
        self.pbar.show()

        # Add a timer callback to update the value of the progress bar
        self.timer = gobject.timeout_add (100, progress_timeout, self)

        separator = gtk.HSeparator()
        vbox.pack_start(separator, False, False, 0)
        separator.show()
        self.pbar.set_text("\t niodsmc djf90w jdsn90d k-0dm \t")
        self.pbar.pulse()


        self.window.show()

def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    ProgressBar()
    main()
