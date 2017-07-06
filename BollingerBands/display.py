# -------------------------------------------------------------------------------
# Generated by PixieDust code generator
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# Inherited from maven-artifact https://github.com/hamnis/maven-artifact
# -------------------------------------------------------------------------------

from pixiedust.display.display import Display
from pixiedust.utils import Logger

from bokeh.plotting import figure, output_notebook, show
from bokeh.palettes import Blues

@Logger()
class BollingerBandsHandler(Display):
    """
        Main Render method
    """
    def doRender(self,handlerId):
        #TODO Add your code here
        #You can use the methods available in base Display class to construct the html markup that will be sent to the output cell
        
        workingPDF = self.entity.copy()
        keyFields = self.options.get("keyFields")
        valueFields = self.options.get("valueFields")
        lineField = self.options.get("line")
        patchFields = self.options.get("patch")

        pArr = patchFields.split(",")
        numPatches = len(pArr)

        colors = Blues[numPatches if numPatches > 2 else 3][::-1]

        output_notebook()
        fig = figure()
        i = 0
        for p in pArr:
            cat = workingPDF[workingPDF['name'] == p]
            fig.patch(cat[keyFields], cat[valueFields], color=colors[i])
            i = i + 1

        cat = workingPDF[workingPDF['name'] == lineField]
        fig.line(cat[keyFields], cat[valueFields], color='red', line_width=4)
        show(fig)
        #genScript, genDiv = components(fig)

        #Add html from a jinja2 template, the file must be located in the templates folder located under this file
        #self._addHTMLTemplate("helloWorld.html")

        #Note: you can embed the HTML directly in the file like so
        #self._addHTMLTemplateString("<div>Hello World</div>")