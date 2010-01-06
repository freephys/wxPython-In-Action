-- Premake script for the wx.NET "Dialogs" sample.
-- See http://premake.sourceforge.net/ for more info about Premake.

package.name     = "minimal"
package.language = "c#"
package.kind     = "winexe"
package.target   = "minimal"

package.links    = { "System.Drawing", "wx.NET" }

package.files    = { "minimal.cs minimal_wdr.cs" }
