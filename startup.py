import qiime2
import pandas as pd
import os
from qiime2.plugins import available_plugins
from IPython.display import display, IFrame, HTML

# Widen the notebook page
display(HTML("<style>.container { width:100% !important; }</style>"))


######################
# Function definitions
######################

# Extracts raw data from artifact
def dumpArtData(qiArtifact):
    exportArtPath = "Exported_Qiime_Artifacts"
    if not os.path.exists(exportArtPath):
        os.mkdir(exportArtPath)
    artName = qiArtifact[:-4]
    artDir = exportArtPath + "/" + artName + "_ART"
    art = qiime2.Artifact.load(qiArtifact)
    qiime2.Artifact.export_data(art, artDir)

# Extract and view visualization in-line
def viewVizData(vzData, fileName="index"):
    exportVizPath = "Exported_Qiime_Visualizations"
    if not os.path.exists(exportVizPath):
        os.mkdir(exportVizPath)
    artName = vzData[:-4]
    vzDir = exportVizPath + "/" + artName + "_vz"
    viz = qiime2.Visualization.load(vzData)
    qiime2.Visualization.export_data(viz, vzDir)

    # Overcomes issue that demux visualization has embedded graphics that won't register in IFrame.
    # Uses assumtion that 'demux' output will have a quality plot present. May cause issues with other visualizations!!!
    # Also, assumes 'index.html' contains main primary graphic. Secondary graphics can be passed using 'file' argument.
    if os.path.exists("".join(vzDir + "/quality-plot.html")) and fileName == "index":
        display(IFrame(src="".join(vzDir + "/overview.html"), width=2150, height=1000))
        display(IFrame(src="".join(vzDir + "/quality-plot.html"), width=2150, height=1000))
    else:
        display(IFrame(src="".join(vzDir + "/" + fileName + ".html"), width=2150, height=1000))
