-- Premake script for the wx.NET "Dialogs" sample.
-- See http://premake.sourceforge.net/ for more info about Premake.

package.name     = "menu"
package.language = "c#"
package.kind     = "winexe"
package.target   = "menu"

package.links    = { "System.Drawing", "wx.NET" }

package.files    = { "menu.cs menu_wdr.cs" }
