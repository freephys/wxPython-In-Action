-- Premake script for the wx.NET "Dialogs" sample.
-- See http://premake.sourceforge.net/ for more info about Premake.

package.name     = "notebook"
package.language = "c#"
package.kind     = "winexe"
package.target   = "notebook"

package.links    = { "System.Drawing", "wx.NET" }

package.files    = { "notebook.cs notebook_wdr.cs" }
