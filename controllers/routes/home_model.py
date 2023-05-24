from typing import Union, Any
from atri_react.TextBox import TextBox
from manifests.ButtonFlex import ButtonFlex
from atri_react.Anchor import Anchor
from manifests.FramerText import FramerText
from atri_react.Flex import Flex
from atri_react.Image import Image
from manifests.Pages import Pages
from manifests.ScaleFlex import ScaleFlex
from manifests.DropdownMenu import DropdownMenu
from manifests.LineText import LineText
from atri_react.Div import Div
from manifests.FramerFlex import FramerFlex


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.TextBox1 = state["TextBox1"] if "TextBox1" in state else None
		self.TextBox2 = state["TextBox2"] if "TextBox2" in state else None
		self.TextBox3 = state["TextBox3"] if "TextBox3" in state else None
		self.TextBox4 = state["TextBox4"] if "TextBox4" in state else None
		self.ButtonFlex1 = state["ButtonFlex1"] if "ButtonFlex1" in state else None
		self.ButtonFlex2 = state["ButtonFlex2"] if "ButtonFlex2" in state else None
		self.Anchor1 = state["Anchor1"] if "Anchor1" in state else None
		self.Anchor2 = state["Anchor2"] if "Anchor2" in state else None
		self.FramerText1 = state["FramerText1"] if "FramerText1" in state else None
		self.FramerText2 = state["FramerText2"] if "FramerText2" in state else None
		self.FramerText3 = state["FramerText3"] if "FramerText3" in state else None
		self.TextBox5 = state["TextBox5"] if "TextBox5" in state else None
		self.TextBox6 = state["TextBox6"] if "TextBox6" in state else None
		self.TextBox7 = state["TextBox7"] if "TextBox7" in state else None
		self.TextBox8 = state["TextBox8"] if "TextBox8" in state else None
		self.Flex1 = state["Flex1"] if "Flex1" in state else None
		self.Flex2 = state["Flex2"] if "Flex2" in state else None
		self.Anchor3 = state["Anchor3"] if "Anchor3" in state else None
		self.Anchor4 = state["Anchor4"] if "Anchor4" in state else None
		self.Anchor5 = state["Anchor5"] if "Anchor5" in state else None
		self.Flex3 = state["Flex3"] if "Flex3" in state else None
		self.FramerText4 = state["FramerText4"] if "FramerText4" in state else None
		self.FramerText5 = state["FramerText5"] if "FramerText5" in state else None
		self.FramerText6 = state["FramerText6"] if "FramerText6" in state else None
		self.FramerText7 = state["FramerText7"] if "FramerText7" in state else None
		self.Image1 = state["Image1"] if "Image1" in state else None
		self.ButtonFlex3 = state["ButtonFlex3"] if "ButtonFlex3" in state else None
		self.ButtonFlex4 = state["ButtonFlex4"] if "ButtonFlex4" in state else None
		self.Flex4 = state["Flex4"] if "Flex4" in state else None
		self.Pages1 = state["Pages1"] if "Pages1" in state else None
		self.Anchor6 = state["Anchor6"] if "Anchor6" in state else None
		self.Anchor7 = state["Anchor7"] if "Anchor7" in state else None
		self.Anchor8 = state["Anchor8"] if "Anchor8" in state else None
		self.Anchor9 = state["Anchor9"] if "Anchor9" in state else None
		self.ScaleFlex1 = state["ScaleFlex1"] if "ScaleFlex1" in state else None
		self.Anchor10 = state["Anchor10"] if "Anchor10" in state else None
		self.Anchor11 = state["Anchor11"] if "Anchor11" in state else None
		self.DropdownMenu1 = state["DropdownMenu1"] if "DropdownMenu1" in state else None
		self.Flex5 = state["Flex5"] if "Flex5" in state else None
		self.Anchor12 = state["Anchor12"] if "Anchor12" in state else None
		self.Flex6 = state["Flex6"] if "Flex6" in state else None
		self.Flex7 = state["Flex7"] if "Flex7" in state else None
		self.Flex8 = state["Flex8"] if "Flex8" in state else None
		self.Flex9 = state["Flex9"] if "Flex9" in state else None
		self.Flex10 = state["Flex10"] if "Flex10" in state else None
		self.Flex11 = state["Flex11"] if "Flex11" in state else None
		self.navbar1 = state["navbar1"] if "navbar1" in state else None
		self.Flex13 = state["Flex13"] if "Flex13" in state else None
		self.TextBox9 = state["TextBox9"] if "TextBox9" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.TextBox11 = state["TextBox11"] if "TextBox11" in state else None
		self.TextBox12 = state["TextBox12"] if "TextBox12" in state else None
		self.ButtonFlex5 = state["ButtonFlex5"] if "ButtonFlex5" in state else None
		self.ButtonFlex6 = state["ButtonFlex6"] if "ButtonFlex6" in state else None
		self.Anchor13 = state["Anchor13"] if "Anchor13" in state else None
		self.Anchor14 = state["Anchor14"] if "Anchor14" in state else None
		self.buttons1 = state["buttons1"] if "buttons1" in state else None
		self.TextBox13 = state["TextBox13"] if "TextBox13" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.TextBox14 = state["TextBox14"] if "TextBox14" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.TextBox15 = state["TextBox15"] if "TextBox15" in state else None
		self.Image4 = state["Image4"] if "Image4" in state else None
		self.TextBox16 = state["TextBox16"] if "TextBox16" in state else None
		self.Image5 = state["Image5"] if "Image5" in state else None
		self.TextBox17 = state["TextBox17"] if "TextBox17" in state else None
		self.Image6 = state["Image6"] if "Image6" in state else None
		self.TextBox18 = state["TextBox18"] if "TextBox18" in state else None
		self.Image7 = state["Image7"] if "Image7" in state else None
		self.FramerText8 = state["FramerText8"] if "FramerText8" in state else None
		self.FramerText9 = state["FramerText9"] if "FramerText9" in state else None
		self.FramerText10 = state["FramerText10"] if "FramerText10" in state else None
		self.FramerText11 = state["FramerText11"] if "FramerText11" in state else None
		self.FramerText12 = state["FramerText12"] if "FramerText12" in state else None
		self.FramerText13 = state["FramerText13"] if "FramerText13" in state else None
		self.FramerText14 = state["FramerText14"] if "FramerText14" in state else None
		self.FramerText15 = state["FramerText15"] if "FramerText15" in state else None
		self.FramerText16 = state["FramerText16"] if "FramerText16" in state else None
		self.FramerText17 = state["FramerText17"] if "FramerText17" in state else None
		self.FramerText18 = state["FramerText18"] if "FramerText18" in state else None
		self.FramerText19 = state["FramerText19"] if "FramerText19" in state else None
		self.FramerText20 = state["FramerText20"] if "FramerText20" in state else None
		self.FramerText21 = state["FramerText21"] if "FramerText21" in state else None
		self.FramerText22 = state["FramerText22"] if "FramerText22" in state else None
		self.FramerText23 = state["FramerText23"] if "FramerText23" in state else None
		self.FramerText24 = state["FramerText24"] if "FramerText24" in state else None
		self.FramerText25 = state["FramerText25"] if "FramerText25" in state else None
		self.FramerText26 = state["FramerText26"] if "FramerText26" in state else None
		self.FramerText27 = state["FramerText27"] if "FramerText27" in state else None
		self.FramerText28 = state["FramerText28"] if "FramerText28" in state else None
		self.FramerText29 = state["FramerText29"] if "FramerText29" in state else None
		self.FramerText30 = state["FramerText30"] if "FramerText30" in state else None
		self.ButtonFlex7 = state["ButtonFlex7"] if "ButtonFlex7" in state else None
		self.ButtonFlex8 = state["ButtonFlex8"] if "ButtonFlex8" in state else None
		self.ButtonFlex9 = state["ButtonFlex9"] if "ButtonFlex9" in state else None
		self.ButtonFlex10 = state["ButtonFlex10"] if "ButtonFlex10" in state else None
		self.ButtonFlex11 = state["ButtonFlex11"] if "ButtonFlex11" in state else None
		self.ButtonFlex12 = state["ButtonFlex12"] if "ButtonFlex12" in state else None
		self.LineText1 = state["LineText1"] if "LineText1" in state else None
		self.FramerText31 = state["FramerText31"] if "FramerText31" in state else None
		self.FramerText32 = state["FramerText32"] if "FramerText32" in state else None
		self.FramerText33 = state["FramerText33"] if "FramerText33" in state else None
		self.FramerText34 = state["FramerText34"] if "FramerText34" in state else None
		self.FramerText35 = state["FramerText35"] if "FramerText35" in state else None
		self.FramerText36 = state["FramerText36"] if "FramerText36" in state else None
		self.FramerText37 = state["FramerText37"] if "FramerText37" in state else None
		self.FramerText38 = state["FramerText38"] if "FramerText38" in state else None
		self.FramerText39 = state["FramerText39"] if "FramerText39" in state else None
		self.FramerText40 = state["FramerText40"] if "FramerText40" in state else None
		self.FramerText41 = state["FramerText41"] if "FramerText41" in state else None
		self.FramerText42 = state["FramerText42"] if "FramerText42" in state else None
		self.Anchor15 = state["Anchor15"] if "Anchor15" in state else None
		self.Anchor16 = state["Anchor16"] if "Anchor16" in state else None
		self.Anchor17 = state["Anchor17"] if "Anchor17" in state else None
		self.Anchor18 = state["Anchor18"] if "Anchor18" in state else None
		self.Anchor19 = state["Anchor19"] if "Anchor19" in state else None
		self.Anchor20 = state["Anchor20"] if "Anchor20" in state else None
		self.Anchor21 = state["Anchor21"] if "Anchor21" in state else None
		self.Anchor22 = state["Anchor22"] if "Anchor22" in state else None
		self.Anchor23 = state["Anchor23"] if "Anchor23" in state else None
		self.Anchor24 = state["Anchor24"] if "Anchor24" in state else None
		self.Anchor25 = state["Anchor25"] if "Anchor25" in state else None
		self.Anchor26 = state["Anchor26"] if "Anchor26" in state else None
		self.Anchor27 = state["Anchor27"] if "Anchor27" in state else None
		self.Anchor28 = state["Anchor28"] if "Anchor28" in state else None
		self.Anchor29 = state["Anchor29"] if "Anchor29" in state else None
		self.Anchor30 = state["Anchor30"] if "Anchor30" in state else None
		self.Anchor31 = state["Anchor31"] if "Anchor31" in state else None
		self.Anchor32 = state["Anchor32"] if "Anchor32" in state else None
		self.Anchor33 = state["Anchor33"] if "Anchor33" in state else None
		self.Anchor34 = state["Anchor34"] if "Anchor34" in state else None
		self.Anchor35 = state["Anchor35"] if "Anchor35" in state else None
		self.Anchor36 = state["Anchor36"] if "Anchor36" in state else None
		self.Anchor37 = state["Anchor37"] if "Anchor37" in state else None
		self.Anchor38 = state["Anchor38"] if "Anchor38" in state else None
		self.Anchor39 = state["Anchor39"] if "Anchor39" in state else None
		self.Anchor40 = state["Anchor40"] if "Anchor40" in state else None
		self.Anchor41 = state["Anchor41"] if "Anchor41" in state else None
		self.Anchor42 = state["Anchor42"] if "Anchor42" in state else None
		self.Anchor43 = state["Anchor43"] if "Anchor43" in state else None
		self.Anchor44 = state["Anchor44"] if "Anchor44" in state else None
		self.Anchor45 = state["Anchor45"] if "Anchor45" in state else None
		self.Anchor46 = state["Anchor46"] if "Anchor46" in state else None
		self.Anchor47 = state["Anchor47"] if "Anchor47" in state else None
		self.Anchor48 = state["Anchor48"] if "Anchor48" in state else None
		self.Anchor49 = state["Anchor49"] if "Anchor49" in state else None
		self.Anchor50 = state["Anchor50"] if "Anchor50" in state else None
		self.Anchor51 = state["Anchor51"] if "Anchor51" in state else None
		self.Anchor52 = state["Anchor52"] if "Anchor52" in state else None
		self.Anchor53 = state["Anchor53"] if "Anchor53" in state else None
		self.Anchor54 = state["Anchor54"] if "Anchor54" in state else None
		self.Anchor55 = state["Anchor55"] if "Anchor55" in state else None
		self.Anchor56 = state["Anchor56"] if "Anchor56" in state else None
		self.Flex16 = state["Flex16"] if "Flex16" in state else None
		self.Flex17 = state["Flex17"] if "Flex17" in state else None
		self.Image8 = state["Image8"] if "Image8" in state else None
		self.FramerText43 = state["FramerText43"] if "FramerText43" in state else None
		self.FramerText44 = state["FramerText44"] if "FramerText44" in state else None
		self.Flex18 = state["Flex18"] if "Flex18" in state else None
		self.TextBox19 = state["TextBox19"] if "TextBox19" in state else None
		self.TextBox20 = state["TextBox20"] if "TextBox20" in state else None
		self.Flex19 = state["Flex19"] if "Flex19" in state else None
		self.TextBox21 = state["TextBox21"] if "TextBox21" in state else None
		self.Flex20 = state["Flex20"] if "Flex20" in state else None
		self.Flex21 = state["Flex21"] if "Flex21" in state else None
		self.TextBox22 = state["TextBox22"] if "TextBox22" in state else None
		self.LineText2 = state["LineText2"] if "LineText2" in state else None
		self.LineText3 = state["LineText3"] if "LineText3" in state else None
		self.ScaleFlex2 = state["ScaleFlex2"] if "ScaleFlex2" in state else None
		self.Anchor57 = state["Anchor57"] if "Anchor57" in state else None
		self.TextBox23 = state["TextBox23"] if "TextBox23" in state else None
		self.Anchor58 = state["Anchor58"] if "Anchor58" in state else None
		self.TextBox24 = state["TextBox24"] if "TextBox24" in state else None
		self.Flex22 = state["Flex22"] if "Flex22" in state else None
		self.Flex23 = state["Flex23"] if "Flex23" in state else None
		self.Flex24 = state["Flex24"] if "Flex24" in state else None
		self.Flex25 = state["Flex25"] if "Flex25" in state else None
		self.Anchor59 = state["Anchor59"] if "Anchor59" in state else None
		self.Anchor60 = state["Anchor60"] if "Anchor60" in state else None
		self.Anchor61 = state["Anchor61"] if "Anchor61" in state else None
		self.TextBox25 = state["TextBox25"] if "TextBox25" in state else None
		self.Flex26 = state["Flex26"] if "Flex26" in state else None
		self.Div1 = state["Div1"] if "Div1" in state else None
		self.Flex27 = state["Flex27"] if "Flex27" in state else None
		self.Flex28 = state["Flex28"] if "Flex28" in state else None
		self.Flex29 = state["Flex29"] if "Flex29" in state else None
		self.Flex30 = state["Flex30"] if "Flex30" in state else None
		self.Flex31 = state["Flex31"] if "Flex31" in state else None
		self.Flex32 = state["Flex32"] if "Flex32" in state else None
		self.Div2 = state["Div2"] if "Div2" in state else None
		self.FramerFlex2 = state["FramerFlex2"] if "FramerFlex2" in state else None
		self.Flex33 = state["Flex33"] if "Flex33" in state else None
		self.footer1 = state["footer1"] if "footer1" in state else None
		self.TextBox26 = state["TextBox26"] if "TextBox26" in state else None
		self.TextBox27 = state["TextBox27"] if "TextBox27" in state else None
		self.Flex35 = state["Flex35"] if "Flex35" in state else None
		self.FramerFlex3 = state["FramerFlex3"] if "FramerFlex3" in state else None
		self.Flex36 = state["Flex36"] if "Flex36" in state else None
		self.Flex37 = state["Flex37"] if "Flex37" in state else None
		self.Flex38 = state["Flex38"] if "Flex38" in state else None
		self.FramerFlex4 = state["FramerFlex4"] if "FramerFlex4" in state else None
		self.Div3 = state["Div3"] if "Div3" in state else None
		self.Flex40 = state["Flex40"] if "Flex40" in state else None
		self.TextBox28 = state["TextBox28"] if "TextBox28" in state else None
		self.TextBox29 = state["TextBox29"] if "TextBox29" in state else None
		self.Flex47 = state["Flex47"] if "Flex47" in state else None
		self.Flex48 = state["Flex48"] if "Flex48" in state else None
		self.Flex49 = state["Flex49"] if "Flex49" in state else None
		self.FramerFlex9 = state["FramerFlex9"] if "FramerFlex9" in state else None
		self.TextBox38 = state["TextBox38"] if "TextBox38" in state else None
		self.TextBox39 = state["TextBox39"] if "TextBox39" in state else None
		self.Flex50 = state["Flex50"] if "Flex50" in state else None
		self.Div8 = state["Div8"] if "Div8" in state else None
		self.TextBox40 = state["TextBox40"] if "TextBox40" in state else None
		self.TextBox41 = state["TextBox41"] if "TextBox41" in state else None
		self.Div9 = state["Div9"] if "Div9" in state else None
		self.Flex51 = state["Flex51"] if "Flex51" in state else None
		self.FramerFlex10 = state["FramerFlex10"] if "FramerFlex10" in state else None
		self.TextBox42 = state["TextBox42"] if "TextBox42" in state else None
		self.TextBox43 = state["TextBox43"] if "TextBox43" in state else None
		self.Div10 = state["Div10"] if "Div10" in state else None
		self.Flex52 = state["Flex52"] if "Flex52" in state else None
		self.FramerFlex11 = state["FramerFlex11"] if "FramerFlex11" in state else None
		self.TextBox45 = state["TextBox45"] if "TextBox45" in state else None
		self.Div11 = state["Div11"] if "Div11" in state else None
		self.Flex53 = state["Flex53"] if "Flex53" in state else None
		self.FramerFlex12 = state["FramerFlex12"] if "FramerFlex12" in state else None
		self.Image10 = state["Image10"] if "Image10" in state else None
		self.Flex54 = state["Flex54"] if "Flex54" in state else None
		self.Flex55 = state["Flex55"] if "Flex55" in state else None
		self.FramerFlex13 = state["FramerFlex13"] if "FramerFlex13" in state else None
		self.Flex56 = state["Flex56"] if "Flex56" in state else None
		self.Div12 = state["Div12"] if "Div12" in state else None
		self.TextBox46 = state["TextBox46"] if "TextBox46" in state else None
		self.Flex57 = state["Flex57"] if "Flex57" in state else None
		self.FramerFlex14 = state["FramerFlex14"] if "FramerFlex14" in state else None
		self.Anchor62 = state["Anchor62"] if "Anchor62" in state else None
		self.ScaleFlex3 = state["ScaleFlex3"] if "ScaleFlex3" in state else None
		self.Image11 = state["Image11"] if "Image11" in state else None
		self.TextBox47 = state["TextBox47"] if "TextBox47" in state else None
		self.TextBox48 = state["TextBox48"] if "TextBox48" in state else None
		self.Image12 = state["Image12"] if "Image12" in state else None
		self.ScaleFlex4 = state["ScaleFlex4"] if "ScaleFlex4" in state else None
		self.Anchor63 = state["Anchor63"] if "Anchor63" in state else None
		self.FramerFlex15 = state["FramerFlex15"] if "FramerFlex15" in state else None
		self.Image13 = state["Image13"] if "Image13" in state else None
		self.TextBox49 = state["TextBox49"] if "TextBox49" in state else None
		self.TextBox50 = state["TextBox50"] if "TextBox50" in state else None
		self.Image14 = state["Image14"] if "Image14" in state else None
		self.ScaleFlex5 = state["ScaleFlex5"] if "ScaleFlex5" in state else None
		self.ScaleFlex6 = state["ScaleFlex6"] if "ScaleFlex6" in state else None
		self.Anchor64 = state["Anchor64"] if "Anchor64" in state else None
		self.Anchor65 = state["Anchor65"] if "Anchor65" in state else None
		self.FramerFlex16 = state["FramerFlex16"] if "FramerFlex16" in state else None
		self.FramerFlex17 = state["FramerFlex17"] if "FramerFlex17" in state else None
		self.Flex58 = state["Flex58"] if "Flex58" in state else None
		self.Image15 = state["Image15"] if "Image15" in state else None
		self.TextBox51 = state["TextBox51"] if "TextBox51" in state else None
		self.TextBox52 = state["TextBox52"] if "TextBox52" in state else None
		self.Image16 = state["Image16"] if "Image16" in state else None
		self.ScaleFlex7 = state["ScaleFlex7"] if "ScaleFlex7" in state else None
		self.ScaleFlex8 = state["ScaleFlex8"] if "ScaleFlex8" in state else None
		self.Anchor66 = state["Anchor66"] if "Anchor66" in state else None
		self.Anchor67 = state["Anchor67"] if "Anchor67" in state else None
		self.FramerFlex18 = state["FramerFlex18"] if "FramerFlex18" in state else None
		self.FramerFlex19 = state["FramerFlex19"] if "FramerFlex19" in state else None
		self.Flex59 = state["Flex59"] if "Flex59" in state else None
		self.Image17 = state["Image17"] if "Image17" in state else None
		self.TextBox53 = state["TextBox53"] if "TextBox53" in state else None
		self.TextBox54 = state["TextBox54"] if "TextBox54" in state else None
		self.Image18 = state["Image18"] if "Image18" in state else None
		self.ScaleFlex9 = state["ScaleFlex9"] if "ScaleFlex9" in state else None
		self.ScaleFlex10 = state["ScaleFlex10"] if "ScaleFlex10" in state else None
		self.Anchor68 = state["Anchor68"] if "Anchor68" in state else None
		self.Anchor69 = state["Anchor69"] if "Anchor69" in state else None
		self.FramerFlex20 = state["FramerFlex20"] if "FramerFlex20" in state else None
		self.FramerFlex21 = state["FramerFlex21"] if "FramerFlex21" in state else None
		self.Flex60 = state["Flex60"] if "Flex60" in state else None
		self.Image19 = state["Image19"] if "Image19" in state else None
		self.TextBox55 = state["TextBox55"] if "TextBox55" in state else None
		self.TextBox56 = state["TextBox56"] if "TextBox56" in state else None
		self.Image20 = state["Image20"] if "Image20" in state else None
		self.ScaleFlex11 = state["ScaleFlex11"] if "ScaleFlex11" in state else None
		self.ScaleFlex12 = state["ScaleFlex12"] if "ScaleFlex12" in state else None
		self.Anchor70 = state["Anchor70"] if "Anchor70" in state else None
		self.Anchor71 = state["Anchor71"] if "Anchor71" in state else None
		self.FramerFlex22 = state["FramerFlex22"] if "FramerFlex22" in state else None
		self.FramerFlex23 = state["FramerFlex23"] if "FramerFlex23" in state else None
		self.Flex61 = state["Flex61"] if "Flex61" in state else None
		self.Image21 = state["Image21"] if "Image21" in state else None
		self.TextBox57 = state["TextBox57"] if "TextBox57" in state else None
		self.TextBox58 = state["TextBox58"] if "TextBox58" in state else None
		self.Image22 = state["Image22"] if "Image22" in state else None
		self.ScaleFlex13 = state["ScaleFlex13"] if "ScaleFlex13" in state else None
		self.ScaleFlex14 = state["ScaleFlex14"] if "ScaleFlex14" in state else None
		self.Anchor72 = state["Anchor72"] if "Anchor72" in state else None
		self.Anchor73 = state["Anchor73"] if "Anchor73" in state else None
		self.FramerFlex24 = state["FramerFlex24"] if "FramerFlex24" in state else None
		self.FramerFlex25 = state["FramerFlex25"] if "FramerFlex25" in state else None
		self.Flex62 = state["Flex62"] if "Flex62" in state else None
		self.Image23 = state["Image23"] if "Image23" in state else None
		self.TextBox59 = state["TextBox59"] if "TextBox59" in state else None
		self.TextBox60 = state["TextBox60"] if "TextBox60" in state else None
		self.Image24 = state["Image24"] if "Image24" in state else None
		self.ScaleFlex15 = state["ScaleFlex15"] if "ScaleFlex15" in state else None
		self.ScaleFlex16 = state["ScaleFlex16"] if "ScaleFlex16" in state else None
		self.Anchor74 = state["Anchor74"] if "Anchor74" in state else None
		self.Anchor75 = state["Anchor75"] if "Anchor75" in state else None
		self.FramerFlex26 = state["FramerFlex26"] if "FramerFlex26" in state else None
		self.FramerFlex27 = state["FramerFlex27"] if "FramerFlex27" in state else None
		self.Flex63 = state["Flex63"] if "Flex63" in state else None
		self.Image25 = state["Image25"] if "Image25" in state else None
		self.TextBox61 = state["TextBox61"] if "TextBox61" in state else None
		self.TextBox62 = state["TextBox62"] if "TextBox62" in state else None
		self.Image26 = state["Image26"] if "Image26" in state else None
		self.ScaleFlex17 = state["ScaleFlex17"] if "ScaleFlex17" in state else None
		self.ScaleFlex18 = state["ScaleFlex18"] if "ScaleFlex18" in state else None
		self.Anchor76 = state["Anchor76"] if "Anchor76" in state else None
		self.Anchor77 = state["Anchor77"] if "Anchor77" in state else None
		self.FramerFlex28 = state["FramerFlex28"] if "FramerFlex28" in state else None
		self.FramerFlex29 = state["FramerFlex29"] if "FramerFlex29" in state else None
		self.Flex64 = state["Flex64"] if "Flex64" in state else None
		self.Image27 = state["Image27"] if "Image27" in state else None
		self.TextBox63 = state["TextBox63"] if "TextBox63" in state else None
		self.TextBox64 = state["TextBox64"] if "TextBox64" in state else None
		self.Image28 = state["Image28"] if "Image28" in state else None
		self.ScaleFlex19 = state["ScaleFlex19"] if "ScaleFlex19" in state else None
		self.ScaleFlex20 = state["ScaleFlex20"] if "ScaleFlex20" in state else None
		self.Anchor78 = state["Anchor78"] if "Anchor78" in state else None
		self.Anchor79 = state["Anchor79"] if "Anchor79" in state else None
		self.FramerFlex30 = state["FramerFlex30"] if "FramerFlex30" in state else None
		self.FramerFlex31 = state["FramerFlex31"] if "FramerFlex31" in state else None
		self.Flex65 = state["Flex65"] if "Flex65" in state else None
		self.Image29 = state["Image29"] if "Image29" in state else None
		self.TextBox65 = state["TextBox65"] if "TextBox65" in state else None
		self.TextBox66 = state["TextBox66"] if "TextBox66" in state else None
		self.Image30 = state["Image30"] if "Image30" in state else None
		self.ScaleFlex21 = state["ScaleFlex21"] if "ScaleFlex21" in state else None
		self.ScaleFlex22 = state["ScaleFlex22"] if "ScaleFlex22" in state else None
		self.Anchor80 = state["Anchor80"] if "Anchor80" in state else None
		self.Anchor81 = state["Anchor81"] if "Anchor81" in state else None
		self.FramerFlex32 = state["FramerFlex32"] if "FramerFlex32" in state else None
		self.FramerFlex33 = state["FramerFlex33"] if "FramerFlex33" in state else None
		self.Flex66 = state["Flex66"] if "Flex66" in state else None
		self.Image31 = state["Image31"] if "Image31" in state else None
		self.TextBox67 = state["TextBox67"] if "TextBox67" in state else None
		self.TextBox68 = state["TextBox68"] if "TextBox68" in state else None
		self.Image32 = state["Image32"] if "Image32" in state else None
		self.ScaleFlex23 = state["ScaleFlex23"] if "ScaleFlex23" in state else None
		self.ScaleFlex24 = state["ScaleFlex24"] if "ScaleFlex24" in state else None
		self.Anchor82 = state["Anchor82"] if "Anchor82" in state else None
		self.Anchor83 = state["Anchor83"] if "Anchor83" in state else None
		self.FramerFlex34 = state["FramerFlex34"] if "FramerFlex34" in state else None
		self.FramerFlex35 = state["FramerFlex35"] if "FramerFlex35" in state else None
		self.Flex67 = state["Flex67"] if "Flex67" in state else None
		self.Image33 = state["Image33"] if "Image33" in state else None
		self.TextBox69 = state["TextBox69"] if "TextBox69" in state else None
		self.TextBox70 = state["TextBox70"] if "TextBox70" in state else None
		self.Image34 = state["Image34"] if "Image34" in state else None
		self.ScaleFlex25 = state["ScaleFlex25"] if "ScaleFlex25" in state else None
		self.ScaleFlex26 = state["ScaleFlex26"] if "ScaleFlex26" in state else None
		self.Anchor84 = state["Anchor84"] if "Anchor84" in state else None
		self.Anchor85 = state["Anchor85"] if "Anchor85" in state else None
		self.FramerFlex36 = state["FramerFlex36"] if "FramerFlex36" in state else None
		self.FramerFlex37 = state["FramerFlex37"] if "FramerFlex37" in state else None
		self.Flex68 = state["Flex68"] if "Flex68" in state else None
		self.TextBox71 = state["TextBox71"] if "TextBox71" in state else None
		self.TextBox72 = state["TextBox72"] if "TextBox72" in state else None
		self.ButtonFlex13 = state["ButtonFlex13"] if "ButtonFlex13" in state else None
		self.Anchor86 = state["Anchor86"] if "Anchor86" in state else None
		self.Flex69 = state["Flex69"] if "Flex69" in state else None
		self.Flex70 = state["Flex70"] if "Flex70" in state else None
		self.Flex71 = state["Flex71"] if "Flex71" in state else None
		self.Flex72 = state["Flex72"] if "Flex72" in state else None
		self.TextBox73 = state["TextBox73"] if "TextBox73" in state else None
		self.Div13 = state["Div13"] if "Div13" in state else None
		self.FramerFlex38 = state["FramerFlex38"] if "FramerFlex38" in state else None
		self.Flex73 = state["Flex73"] if "Flex73" in state else None
		self.Image35 = state["Image35"] if "Image35" in state else None
		self.TextBox74 = state["TextBox74"] if "TextBox74" in state else None
		self.TextBox75 = state["TextBox75"] if "TextBox75" in state else None
		self.Image36 = state["Image36"] if "Image36" in state else None
		self.ScaleFlex27 = state["ScaleFlex27"] if "ScaleFlex27" in state else None
		self.ScaleFlex28 = state["ScaleFlex28"] if "ScaleFlex28" in state else None
		self.Anchor87 = state["Anchor87"] if "Anchor87" in state else None
		self.Anchor88 = state["Anchor88"] if "Anchor88" in state else None
		self.FramerFlex39 = state["FramerFlex39"] if "FramerFlex39" in state else None
		self.FramerFlex40 = state["FramerFlex40"] if "FramerFlex40" in state else None
		self.Flex74 = state["Flex74"] if "Flex74" in state else None
		self.Image37 = state["Image37"] if "Image37" in state else None
		self.TextBox76 = state["TextBox76"] if "TextBox76" in state else None
		self.TextBox77 = state["TextBox77"] if "TextBox77" in state else None
		self.Image38 = state["Image38"] if "Image38" in state else None
		self.ScaleFlex29 = state["ScaleFlex29"] if "ScaleFlex29" in state else None
		self.ScaleFlex30 = state["ScaleFlex30"] if "ScaleFlex30" in state else None
		self.Anchor89 = state["Anchor89"] if "Anchor89" in state else None
		self.Anchor90 = state["Anchor90"] if "Anchor90" in state else None
		self.FramerFlex41 = state["FramerFlex41"] if "FramerFlex41" in state else None
		self.FramerFlex42 = state["FramerFlex42"] if "FramerFlex42" in state else None
		self.Flex75 = state["Flex75"] if "Flex75" in state else None
		self.Image39 = state["Image39"] if "Image39" in state else None
		self.TextBox78 = state["TextBox78"] if "TextBox78" in state else None
		self.TextBox79 = state["TextBox79"] if "TextBox79" in state else None
		self.Image40 = state["Image40"] if "Image40" in state else None
		self.ScaleFlex31 = state["ScaleFlex31"] if "ScaleFlex31" in state else None
		self.ScaleFlex32 = state["ScaleFlex32"] if "ScaleFlex32" in state else None
		self.Anchor91 = state["Anchor91"] if "Anchor91" in state else None
		self.Anchor92 = state["Anchor92"] if "Anchor92" in state else None
		self.FramerFlex43 = state["FramerFlex43"] if "FramerFlex43" in state else None
		self.FramerFlex44 = state["FramerFlex44"] if "FramerFlex44" in state else None
		self.Flex76 = state["Flex76"] if "Flex76" in state else None
		self.Image41 = state["Image41"] if "Image41" in state else None
		self.TextBox80 = state["TextBox80"] if "TextBox80" in state else None
		self.TextBox81 = state["TextBox81"] if "TextBox81" in state else None
		self.Image42 = state["Image42"] if "Image42" in state else None
		self.ScaleFlex33 = state["ScaleFlex33"] if "ScaleFlex33" in state else None
		self.ScaleFlex34 = state["ScaleFlex34"] if "ScaleFlex34" in state else None
		self.Anchor93 = state["Anchor93"] if "Anchor93" in state else None
		self.Anchor94 = state["Anchor94"] if "Anchor94" in state else None
		self.FramerFlex45 = state["FramerFlex45"] if "FramerFlex45" in state else None
		self.FramerFlex46 = state["FramerFlex46"] if "FramerFlex46" in state else None
		self.Flex77 = state["Flex77"] if "Flex77" in state else None
		self.TextBox84 = state["TextBox84"] if "TextBox84" in state else None
		self.TextBox85 = state["TextBox85"] if "TextBox85" in state else None
		self.ButtonFlex14 = state["ButtonFlex14"] if "ButtonFlex14" in state else None
		self.Anchor97 = state["Anchor97"] if "Anchor97" in state else None
		self.Flex79 = state["Flex79"] if "Flex79" in state else None
		self.Flex80 = state["Flex80"] if "Flex80" in state else None
		self.FramerFlex49 = state["FramerFlex49"] if "FramerFlex49" in state else None
		self.Flex81 = state["Flex81"] if "Flex81" in state else None
		self.Flex82 = state["Flex82"] if "Flex82" in state else None
		self.TextBox86 = state["TextBox86"] if "TextBox86" in state else None
		self.TextBox87 = state["TextBox87"] if "TextBox87" in state else None
		self.TextBox88 = state["TextBox88"] if "TextBox88" in state else None
		self.ButtonFlex15 = state["ButtonFlex15"] if "ButtonFlex15" in state else None
		self.Anchor98 = state["Anchor98"] if "Anchor98" in state else None
		self._setter_access_tracker = {}
		self._getter_access_tracker = {}
  
	def set_event(self, event):
		self.event_data = event["event_data"]
		self.event_alias = event["alias"]
		callback_name = event["callback_name"]
		if hasattr(self, self.event_alias):
			comp = getattr(self, self.event_alias)
			setattr(comp, callback_name, True)
		self.event_repeating = event["repeating"]
  
	
	@property
	def TextBox1(self):
		self._getter_access_tracker["TextBox1"] = {}
		return self._TextBox1
	@TextBox1.setter
	def TextBox1(self, new_state):
		self._setter_access_tracker["TextBox1"] = {}
		self._TextBox1 = TextBox(new_state)

	@property
	def TextBox2(self):
		self._getter_access_tracker["TextBox2"] = {}
		return self._TextBox2
	@TextBox2.setter
	def TextBox2(self, new_state):
		self._setter_access_tracker["TextBox2"] = {}
		self._TextBox2 = TextBox(new_state)

	@property
	def TextBox3(self):
		self._getter_access_tracker["TextBox3"] = {}
		return self._TextBox3
	@TextBox3.setter
	def TextBox3(self, new_state):
		self._setter_access_tracker["TextBox3"] = {}
		self._TextBox3 = TextBox(new_state)

	@property
	def TextBox4(self):
		self._getter_access_tracker["TextBox4"] = {}
		return self._TextBox4
	@TextBox4.setter
	def TextBox4(self, new_state):
		self._setter_access_tracker["TextBox4"] = {}
		self._TextBox4 = TextBox(new_state)

	@property
	def ButtonFlex1(self):
		self._getter_access_tracker["ButtonFlex1"] = {}
		return self._ButtonFlex1
	@ButtonFlex1.setter
	def ButtonFlex1(self, new_state):
		self._setter_access_tracker["ButtonFlex1"] = {}
		self._ButtonFlex1 = ButtonFlex(new_state)

	@property
	def ButtonFlex2(self):
		self._getter_access_tracker["ButtonFlex2"] = {}
		return self._ButtonFlex2
	@ButtonFlex2.setter
	def ButtonFlex2(self, new_state):
		self._setter_access_tracker["ButtonFlex2"] = {}
		self._ButtonFlex2 = ButtonFlex(new_state)

	@property
	def Anchor1(self):
		self._getter_access_tracker["Anchor1"] = {}
		return self._Anchor1
	@Anchor1.setter
	def Anchor1(self, new_state):
		self._setter_access_tracker["Anchor1"] = {}
		self._Anchor1 = Anchor(new_state)

	@property
	def Anchor2(self):
		self._getter_access_tracker["Anchor2"] = {}
		return self._Anchor2
	@Anchor2.setter
	def Anchor2(self, new_state):
		self._setter_access_tracker["Anchor2"] = {}
		self._Anchor2 = Anchor(new_state)

	@property
	def FramerText1(self):
		self._getter_access_tracker["FramerText1"] = {}
		return self._FramerText1
	@FramerText1.setter
	def FramerText1(self, new_state):
		self._setter_access_tracker["FramerText1"] = {}
		self._FramerText1 = FramerText(new_state)

	@property
	def FramerText2(self):
		self._getter_access_tracker["FramerText2"] = {}
		return self._FramerText2
	@FramerText2.setter
	def FramerText2(self, new_state):
		self._setter_access_tracker["FramerText2"] = {}
		self._FramerText2 = FramerText(new_state)

	@property
	def FramerText3(self):
		self._getter_access_tracker["FramerText3"] = {}
		return self._FramerText3
	@FramerText3.setter
	def FramerText3(self, new_state):
		self._setter_access_tracker["FramerText3"] = {}
		self._FramerText3 = FramerText(new_state)

	@property
	def TextBox5(self):
		self._getter_access_tracker["TextBox5"] = {}
		return self._TextBox5
	@TextBox5.setter
	def TextBox5(self, new_state):
		self._setter_access_tracker["TextBox5"] = {}
		self._TextBox5 = TextBox(new_state)

	@property
	def TextBox6(self):
		self._getter_access_tracker["TextBox6"] = {}
		return self._TextBox6
	@TextBox6.setter
	def TextBox6(self, new_state):
		self._setter_access_tracker["TextBox6"] = {}
		self._TextBox6 = TextBox(new_state)

	@property
	def TextBox7(self):
		self._getter_access_tracker["TextBox7"] = {}
		return self._TextBox7
	@TextBox7.setter
	def TextBox7(self, new_state):
		self._setter_access_tracker["TextBox7"] = {}
		self._TextBox7 = TextBox(new_state)

	@property
	def TextBox8(self):
		self._getter_access_tracker["TextBox8"] = {}
		return self._TextBox8
	@TextBox8.setter
	def TextBox8(self, new_state):
		self._setter_access_tracker["TextBox8"] = {}
		self._TextBox8 = TextBox(new_state)

	@property
	def Flex1(self):
		self._getter_access_tracker["Flex1"] = {}
		return self._Flex1
	@Flex1.setter
	def Flex1(self, new_state):
		self._setter_access_tracker["Flex1"] = {}
		self._Flex1 = Flex(new_state)

	@property
	def Flex2(self):
		self._getter_access_tracker["Flex2"] = {}
		return self._Flex2
	@Flex2.setter
	def Flex2(self, new_state):
		self._setter_access_tracker["Flex2"] = {}
		self._Flex2 = Flex(new_state)

	@property
	def Anchor3(self):
		self._getter_access_tracker["Anchor3"] = {}
		return self._Anchor3
	@Anchor3.setter
	def Anchor3(self, new_state):
		self._setter_access_tracker["Anchor3"] = {}
		self._Anchor3 = Anchor(new_state)

	@property
	def Anchor4(self):
		self._getter_access_tracker["Anchor4"] = {}
		return self._Anchor4
	@Anchor4.setter
	def Anchor4(self, new_state):
		self._setter_access_tracker["Anchor4"] = {}
		self._Anchor4 = Anchor(new_state)

	@property
	def Anchor5(self):
		self._getter_access_tracker["Anchor5"] = {}
		return self._Anchor5
	@Anchor5.setter
	def Anchor5(self, new_state):
		self._setter_access_tracker["Anchor5"] = {}
		self._Anchor5 = Anchor(new_state)

	@property
	def Flex3(self):
		self._getter_access_tracker["Flex3"] = {}
		return self._Flex3
	@Flex3.setter
	def Flex3(self, new_state):
		self._setter_access_tracker["Flex3"] = {}
		self._Flex3 = Flex(new_state)

	@property
	def FramerText4(self):
		self._getter_access_tracker["FramerText4"] = {}
		return self._FramerText4
	@FramerText4.setter
	def FramerText4(self, new_state):
		self._setter_access_tracker["FramerText4"] = {}
		self._FramerText4 = FramerText(new_state)

	@property
	def FramerText5(self):
		self._getter_access_tracker["FramerText5"] = {}
		return self._FramerText5
	@FramerText5.setter
	def FramerText5(self, new_state):
		self._setter_access_tracker["FramerText5"] = {}
		self._FramerText5 = FramerText(new_state)

	@property
	def FramerText6(self):
		self._getter_access_tracker["FramerText6"] = {}
		return self._FramerText6
	@FramerText6.setter
	def FramerText6(self, new_state):
		self._setter_access_tracker["FramerText6"] = {}
		self._FramerText6 = FramerText(new_state)

	@property
	def FramerText7(self):
		self._getter_access_tracker["FramerText7"] = {}
		return self._FramerText7
	@FramerText7.setter
	def FramerText7(self, new_state):
		self._setter_access_tracker["FramerText7"] = {}
		self._FramerText7 = FramerText(new_state)

	@property
	def Image1(self):
		self._getter_access_tracker["Image1"] = {}
		return self._Image1
	@Image1.setter
	def Image1(self, new_state):
		self._setter_access_tracker["Image1"] = {}
		self._Image1 = Image(new_state)

	@property
	def ButtonFlex3(self):
		self._getter_access_tracker["ButtonFlex3"] = {}
		return self._ButtonFlex3
	@ButtonFlex3.setter
	def ButtonFlex3(self, new_state):
		self._setter_access_tracker["ButtonFlex3"] = {}
		self._ButtonFlex3 = ButtonFlex(new_state)

	@property
	def ButtonFlex4(self):
		self._getter_access_tracker["ButtonFlex4"] = {}
		return self._ButtonFlex4
	@ButtonFlex4.setter
	def ButtonFlex4(self, new_state):
		self._setter_access_tracker["ButtonFlex4"] = {}
		self._ButtonFlex4 = ButtonFlex(new_state)

	@property
	def Flex4(self):
		self._getter_access_tracker["Flex4"] = {}
		return self._Flex4
	@Flex4.setter
	def Flex4(self, new_state):
		self._setter_access_tracker["Flex4"] = {}
		self._Flex4 = Flex(new_state)

	@property
	def Pages1(self):
		self._getter_access_tracker["Pages1"] = {}
		return self._Pages1
	@Pages1.setter
	def Pages1(self, new_state):
		self._setter_access_tracker["Pages1"] = {}
		self._Pages1 = Pages(new_state)

	@property
	def Anchor6(self):
		self._getter_access_tracker["Anchor6"] = {}
		return self._Anchor6
	@Anchor6.setter
	def Anchor6(self, new_state):
		self._setter_access_tracker["Anchor6"] = {}
		self._Anchor6 = Anchor(new_state)

	@property
	def Anchor7(self):
		self._getter_access_tracker["Anchor7"] = {}
		return self._Anchor7
	@Anchor7.setter
	def Anchor7(self, new_state):
		self._setter_access_tracker["Anchor7"] = {}
		self._Anchor7 = Anchor(new_state)

	@property
	def Anchor8(self):
		self._getter_access_tracker["Anchor8"] = {}
		return self._Anchor8
	@Anchor8.setter
	def Anchor8(self, new_state):
		self._setter_access_tracker["Anchor8"] = {}
		self._Anchor8 = Anchor(new_state)

	@property
	def Anchor9(self):
		self._getter_access_tracker["Anchor9"] = {}
		return self._Anchor9
	@Anchor9.setter
	def Anchor9(self, new_state):
		self._setter_access_tracker["Anchor9"] = {}
		self._Anchor9 = Anchor(new_state)

	@property
	def ScaleFlex1(self):
		self._getter_access_tracker["ScaleFlex1"] = {}
		return self._ScaleFlex1
	@ScaleFlex1.setter
	def ScaleFlex1(self, new_state):
		self._setter_access_tracker["ScaleFlex1"] = {}
		self._ScaleFlex1 = ScaleFlex(new_state)

	@property
	def Anchor10(self):
		self._getter_access_tracker["Anchor10"] = {}
		return self._Anchor10
	@Anchor10.setter
	def Anchor10(self, new_state):
		self._setter_access_tracker["Anchor10"] = {}
		self._Anchor10 = Anchor(new_state)

	@property
	def Anchor11(self):
		self._getter_access_tracker["Anchor11"] = {}
		return self._Anchor11
	@Anchor11.setter
	def Anchor11(self, new_state):
		self._setter_access_tracker["Anchor11"] = {}
		self._Anchor11 = Anchor(new_state)

	@property
	def DropdownMenu1(self):
		self._getter_access_tracker["DropdownMenu1"] = {}
		return self._DropdownMenu1
	@DropdownMenu1.setter
	def DropdownMenu1(self, new_state):
		self._setter_access_tracker["DropdownMenu1"] = {}
		self._DropdownMenu1 = DropdownMenu(new_state)

	@property
	def Flex5(self):
		self._getter_access_tracker["Flex5"] = {}
		return self._Flex5
	@Flex5.setter
	def Flex5(self, new_state):
		self._setter_access_tracker["Flex5"] = {}
		self._Flex5 = Flex(new_state)

	@property
	def Anchor12(self):
		self._getter_access_tracker["Anchor12"] = {}
		return self._Anchor12
	@Anchor12.setter
	def Anchor12(self, new_state):
		self._setter_access_tracker["Anchor12"] = {}
		self._Anchor12 = Anchor(new_state)

	@property
	def Flex6(self):
		self._getter_access_tracker["Flex6"] = {}
		return self._Flex6
	@Flex6.setter
	def Flex6(self, new_state):
		self._setter_access_tracker["Flex6"] = {}
		self._Flex6 = Flex(new_state)

	@property
	def Flex7(self):
		self._getter_access_tracker["Flex7"] = {}
		return self._Flex7
	@Flex7.setter
	def Flex7(self, new_state):
		self._setter_access_tracker["Flex7"] = {}
		self._Flex7 = Flex(new_state)

	@property
	def Flex8(self):
		self._getter_access_tracker["Flex8"] = {}
		return self._Flex8
	@Flex8.setter
	def Flex8(self, new_state):
		self._setter_access_tracker["Flex8"] = {}
		self._Flex8 = Flex(new_state)

	@property
	def Flex9(self):
		self._getter_access_tracker["Flex9"] = {}
		return self._Flex9
	@Flex9.setter
	def Flex9(self, new_state):
		self._setter_access_tracker["Flex9"] = {}
		self._Flex9 = Flex(new_state)

	@property
	def Flex10(self):
		self._getter_access_tracker["Flex10"] = {}
		return self._Flex10
	@Flex10.setter
	def Flex10(self, new_state):
		self._setter_access_tracker["Flex10"] = {}
		self._Flex10 = Flex(new_state)

	@property
	def Flex11(self):
		self._getter_access_tracker["Flex11"] = {}
		return self._Flex11
	@Flex11.setter
	def Flex11(self, new_state):
		self._setter_access_tracker["Flex11"] = {}
		self._Flex11 = Flex(new_state)

	@property
	def navbar1(self):
		self._getter_access_tracker["navbar1"] = {}
		return self._navbar1
	@navbar1.setter
	def navbar1(self, new_state):
		self._setter_access_tracker["navbar1"] = {}
		self._navbar1 = Flex(new_state)

	@property
	def Flex13(self):
		self._getter_access_tracker["Flex13"] = {}
		return self._Flex13
	@Flex13.setter
	def Flex13(self, new_state):
		self._setter_access_tracker["Flex13"] = {}
		self._Flex13 = Flex(new_state)

	@property
	def TextBox9(self):
		self._getter_access_tracker["TextBox9"] = {}
		return self._TextBox9
	@TextBox9.setter
	def TextBox9(self, new_state):
		self._setter_access_tracker["TextBox9"] = {}
		self._TextBox9 = TextBox(new_state)

	@property
	def TextBox10(self):
		self._getter_access_tracker["TextBox10"] = {}
		return self._TextBox10
	@TextBox10.setter
	def TextBox10(self, new_state):
		self._setter_access_tracker["TextBox10"] = {}
		self._TextBox10 = TextBox(new_state)

	@property
	def TextBox11(self):
		self._getter_access_tracker["TextBox11"] = {}
		return self._TextBox11
	@TextBox11.setter
	def TextBox11(self, new_state):
		self._setter_access_tracker["TextBox11"] = {}
		self._TextBox11 = TextBox(new_state)

	@property
	def TextBox12(self):
		self._getter_access_tracker["TextBox12"] = {}
		return self._TextBox12
	@TextBox12.setter
	def TextBox12(self, new_state):
		self._setter_access_tracker["TextBox12"] = {}
		self._TextBox12 = TextBox(new_state)

	@property
	def ButtonFlex5(self):
		self._getter_access_tracker["ButtonFlex5"] = {}
		return self._ButtonFlex5
	@ButtonFlex5.setter
	def ButtonFlex5(self, new_state):
		self._setter_access_tracker["ButtonFlex5"] = {}
		self._ButtonFlex5 = ButtonFlex(new_state)

	@property
	def ButtonFlex6(self):
		self._getter_access_tracker["ButtonFlex6"] = {}
		return self._ButtonFlex6
	@ButtonFlex6.setter
	def ButtonFlex6(self, new_state):
		self._setter_access_tracker["ButtonFlex6"] = {}
		self._ButtonFlex6 = ButtonFlex(new_state)

	@property
	def Anchor13(self):
		self._getter_access_tracker["Anchor13"] = {}
		return self._Anchor13
	@Anchor13.setter
	def Anchor13(self, new_state):
		self._setter_access_tracker["Anchor13"] = {}
		self._Anchor13 = Anchor(new_state)

	@property
	def Anchor14(self):
		self._getter_access_tracker["Anchor14"] = {}
		return self._Anchor14
	@Anchor14.setter
	def Anchor14(self, new_state):
		self._setter_access_tracker["Anchor14"] = {}
		self._Anchor14 = Anchor(new_state)

	@property
	def buttons1(self):
		self._getter_access_tracker["buttons1"] = {}
		return self._buttons1
	@buttons1.setter
	def buttons1(self, new_state):
		self._setter_access_tracker["buttons1"] = {}
		self._buttons1 = Flex(new_state)

	@property
	def TextBox13(self):
		self._getter_access_tracker["TextBox13"] = {}
		return self._TextBox13
	@TextBox13.setter
	def TextBox13(self, new_state):
		self._setter_access_tracker["TextBox13"] = {}
		self._TextBox13 = TextBox(new_state)

	@property
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

	@property
	def TextBox14(self):
		self._getter_access_tracker["TextBox14"] = {}
		return self._TextBox14
	@TextBox14.setter
	def TextBox14(self, new_state):
		self._setter_access_tracker["TextBox14"] = {}
		self._TextBox14 = TextBox(new_state)

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		self._Image3 = Image(new_state)

	@property
	def TextBox15(self):
		self._getter_access_tracker["TextBox15"] = {}
		return self._TextBox15
	@TextBox15.setter
	def TextBox15(self, new_state):
		self._setter_access_tracker["TextBox15"] = {}
		self._TextBox15 = TextBox(new_state)

	@property
	def Image4(self):
		self._getter_access_tracker["Image4"] = {}
		return self._Image4
	@Image4.setter
	def Image4(self, new_state):
		self._setter_access_tracker["Image4"] = {}
		self._Image4 = Image(new_state)

	@property
	def TextBox16(self):
		self._getter_access_tracker["TextBox16"] = {}
		return self._TextBox16
	@TextBox16.setter
	def TextBox16(self, new_state):
		self._setter_access_tracker["TextBox16"] = {}
		self._TextBox16 = TextBox(new_state)

	@property
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		self._Image5 = Image(new_state)

	@property
	def TextBox17(self):
		self._getter_access_tracker["TextBox17"] = {}
		return self._TextBox17
	@TextBox17.setter
	def TextBox17(self, new_state):
		self._setter_access_tracker["TextBox17"] = {}
		self._TextBox17 = TextBox(new_state)

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		self._Image6 = Image(new_state)

	@property
	def TextBox18(self):
		self._getter_access_tracker["TextBox18"] = {}
		return self._TextBox18
	@TextBox18.setter
	def TextBox18(self, new_state):
		self._setter_access_tracker["TextBox18"] = {}
		self._TextBox18 = TextBox(new_state)

	@property
	def Image7(self):
		self._getter_access_tracker["Image7"] = {}
		return self._Image7
	@Image7.setter
	def Image7(self, new_state):
		self._setter_access_tracker["Image7"] = {}
		self._Image7 = Image(new_state)

	@property
	def FramerText8(self):
		self._getter_access_tracker["FramerText8"] = {}
		return self._FramerText8
	@FramerText8.setter
	def FramerText8(self, new_state):
		self._setter_access_tracker["FramerText8"] = {}
		self._FramerText8 = FramerText(new_state)

	@property
	def FramerText9(self):
		self._getter_access_tracker["FramerText9"] = {}
		return self._FramerText9
	@FramerText9.setter
	def FramerText9(self, new_state):
		self._setter_access_tracker["FramerText9"] = {}
		self._FramerText9 = FramerText(new_state)

	@property
	def FramerText10(self):
		self._getter_access_tracker["FramerText10"] = {}
		return self._FramerText10
	@FramerText10.setter
	def FramerText10(self, new_state):
		self._setter_access_tracker["FramerText10"] = {}
		self._FramerText10 = FramerText(new_state)

	@property
	def FramerText11(self):
		self._getter_access_tracker["FramerText11"] = {}
		return self._FramerText11
	@FramerText11.setter
	def FramerText11(self, new_state):
		self._setter_access_tracker["FramerText11"] = {}
		self._FramerText11 = FramerText(new_state)

	@property
	def FramerText12(self):
		self._getter_access_tracker["FramerText12"] = {}
		return self._FramerText12
	@FramerText12.setter
	def FramerText12(self, new_state):
		self._setter_access_tracker["FramerText12"] = {}
		self._FramerText12 = FramerText(new_state)

	@property
	def FramerText13(self):
		self._getter_access_tracker["FramerText13"] = {}
		return self._FramerText13
	@FramerText13.setter
	def FramerText13(self, new_state):
		self._setter_access_tracker["FramerText13"] = {}
		self._FramerText13 = FramerText(new_state)

	@property
	def FramerText14(self):
		self._getter_access_tracker["FramerText14"] = {}
		return self._FramerText14
	@FramerText14.setter
	def FramerText14(self, new_state):
		self._setter_access_tracker["FramerText14"] = {}
		self._FramerText14 = FramerText(new_state)

	@property
	def FramerText15(self):
		self._getter_access_tracker["FramerText15"] = {}
		return self._FramerText15
	@FramerText15.setter
	def FramerText15(self, new_state):
		self._setter_access_tracker["FramerText15"] = {}
		self._FramerText15 = FramerText(new_state)

	@property
	def FramerText16(self):
		self._getter_access_tracker["FramerText16"] = {}
		return self._FramerText16
	@FramerText16.setter
	def FramerText16(self, new_state):
		self._setter_access_tracker["FramerText16"] = {}
		self._FramerText16 = FramerText(new_state)

	@property
	def FramerText17(self):
		self._getter_access_tracker["FramerText17"] = {}
		return self._FramerText17
	@FramerText17.setter
	def FramerText17(self, new_state):
		self._setter_access_tracker["FramerText17"] = {}
		self._FramerText17 = FramerText(new_state)

	@property
	def FramerText18(self):
		self._getter_access_tracker["FramerText18"] = {}
		return self._FramerText18
	@FramerText18.setter
	def FramerText18(self, new_state):
		self._setter_access_tracker["FramerText18"] = {}
		self._FramerText18 = FramerText(new_state)

	@property
	def FramerText19(self):
		self._getter_access_tracker["FramerText19"] = {}
		return self._FramerText19
	@FramerText19.setter
	def FramerText19(self, new_state):
		self._setter_access_tracker["FramerText19"] = {}
		self._FramerText19 = FramerText(new_state)

	@property
	def FramerText20(self):
		self._getter_access_tracker["FramerText20"] = {}
		return self._FramerText20
	@FramerText20.setter
	def FramerText20(self, new_state):
		self._setter_access_tracker["FramerText20"] = {}
		self._FramerText20 = FramerText(new_state)

	@property
	def FramerText21(self):
		self._getter_access_tracker["FramerText21"] = {}
		return self._FramerText21
	@FramerText21.setter
	def FramerText21(self, new_state):
		self._setter_access_tracker["FramerText21"] = {}
		self._FramerText21 = FramerText(new_state)

	@property
	def FramerText22(self):
		self._getter_access_tracker["FramerText22"] = {}
		return self._FramerText22
	@FramerText22.setter
	def FramerText22(self, new_state):
		self._setter_access_tracker["FramerText22"] = {}
		self._FramerText22 = FramerText(new_state)

	@property
	def FramerText23(self):
		self._getter_access_tracker["FramerText23"] = {}
		return self._FramerText23
	@FramerText23.setter
	def FramerText23(self, new_state):
		self._setter_access_tracker["FramerText23"] = {}
		self._FramerText23 = FramerText(new_state)

	@property
	def FramerText24(self):
		self._getter_access_tracker["FramerText24"] = {}
		return self._FramerText24
	@FramerText24.setter
	def FramerText24(self, new_state):
		self._setter_access_tracker["FramerText24"] = {}
		self._FramerText24 = FramerText(new_state)

	@property
	def FramerText25(self):
		self._getter_access_tracker["FramerText25"] = {}
		return self._FramerText25
	@FramerText25.setter
	def FramerText25(self, new_state):
		self._setter_access_tracker["FramerText25"] = {}
		self._FramerText25 = FramerText(new_state)

	@property
	def FramerText26(self):
		self._getter_access_tracker["FramerText26"] = {}
		return self._FramerText26
	@FramerText26.setter
	def FramerText26(self, new_state):
		self._setter_access_tracker["FramerText26"] = {}
		self._FramerText26 = FramerText(new_state)

	@property
	def FramerText27(self):
		self._getter_access_tracker["FramerText27"] = {}
		return self._FramerText27
	@FramerText27.setter
	def FramerText27(self, new_state):
		self._setter_access_tracker["FramerText27"] = {}
		self._FramerText27 = FramerText(new_state)

	@property
	def FramerText28(self):
		self._getter_access_tracker["FramerText28"] = {}
		return self._FramerText28
	@FramerText28.setter
	def FramerText28(self, new_state):
		self._setter_access_tracker["FramerText28"] = {}
		self._FramerText28 = FramerText(new_state)

	@property
	def FramerText29(self):
		self._getter_access_tracker["FramerText29"] = {}
		return self._FramerText29
	@FramerText29.setter
	def FramerText29(self, new_state):
		self._setter_access_tracker["FramerText29"] = {}
		self._FramerText29 = FramerText(new_state)

	@property
	def FramerText30(self):
		self._getter_access_tracker["FramerText30"] = {}
		return self._FramerText30
	@FramerText30.setter
	def FramerText30(self, new_state):
		self._setter_access_tracker["FramerText30"] = {}
		self._FramerText30 = FramerText(new_state)

	@property
	def ButtonFlex7(self):
		self._getter_access_tracker["ButtonFlex7"] = {}
		return self._ButtonFlex7
	@ButtonFlex7.setter
	def ButtonFlex7(self, new_state):
		self._setter_access_tracker["ButtonFlex7"] = {}
		self._ButtonFlex7 = ButtonFlex(new_state)

	@property
	def ButtonFlex8(self):
		self._getter_access_tracker["ButtonFlex8"] = {}
		return self._ButtonFlex8
	@ButtonFlex8.setter
	def ButtonFlex8(self, new_state):
		self._setter_access_tracker["ButtonFlex8"] = {}
		self._ButtonFlex8 = ButtonFlex(new_state)

	@property
	def ButtonFlex9(self):
		self._getter_access_tracker["ButtonFlex9"] = {}
		return self._ButtonFlex9
	@ButtonFlex9.setter
	def ButtonFlex9(self, new_state):
		self._setter_access_tracker["ButtonFlex9"] = {}
		self._ButtonFlex9 = ButtonFlex(new_state)

	@property
	def ButtonFlex10(self):
		self._getter_access_tracker["ButtonFlex10"] = {}
		return self._ButtonFlex10
	@ButtonFlex10.setter
	def ButtonFlex10(self, new_state):
		self._setter_access_tracker["ButtonFlex10"] = {}
		self._ButtonFlex10 = ButtonFlex(new_state)

	@property
	def ButtonFlex11(self):
		self._getter_access_tracker["ButtonFlex11"] = {}
		return self._ButtonFlex11
	@ButtonFlex11.setter
	def ButtonFlex11(self, new_state):
		self._setter_access_tracker["ButtonFlex11"] = {}
		self._ButtonFlex11 = ButtonFlex(new_state)

	@property
	def ButtonFlex12(self):
		self._getter_access_tracker["ButtonFlex12"] = {}
		return self._ButtonFlex12
	@ButtonFlex12.setter
	def ButtonFlex12(self, new_state):
		self._setter_access_tracker["ButtonFlex12"] = {}
		self._ButtonFlex12 = ButtonFlex(new_state)

	@property
	def LineText1(self):
		self._getter_access_tracker["LineText1"] = {}
		return self._LineText1
	@LineText1.setter
	def LineText1(self, new_state):
		self._setter_access_tracker["LineText1"] = {}
		self._LineText1 = LineText(new_state)

	@property
	def FramerText31(self):
		self._getter_access_tracker["FramerText31"] = {}
		return self._FramerText31
	@FramerText31.setter
	def FramerText31(self, new_state):
		self._setter_access_tracker["FramerText31"] = {}
		self._FramerText31 = FramerText(new_state)

	@property
	def FramerText32(self):
		self._getter_access_tracker["FramerText32"] = {}
		return self._FramerText32
	@FramerText32.setter
	def FramerText32(self, new_state):
		self._setter_access_tracker["FramerText32"] = {}
		self._FramerText32 = FramerText(new_state)

	@property
	def FramerText33(self):
		self._getter_access_tracker["FramerText33"] = {}
		return self._FramerText33
	@FramerText33.setter
	def FramerText33(self, new_state):
		self._setter_access_tracker["FramerText33"] = {}
		self._FramerText33 = FramerText(new_state)

	@property
	def FramerText34(self):
		self._getter_access_tracker["FramerText34"] = {}
		return self._FramerText34
	@FramerText34.setter
	def FramerText34(self, new_state):
		self._setter_access_tracker["FramerText34"] = {}
		self._FramerText34 = FramerText(new_state)

	@property
	def FramerText35(self):
		self._getter_access_tracker["FramerText35"] = {}
		return self._FramerText35
	@FramerText35.setter
	def FramerText35(self, new_state):
		self._setter_access_tracker["FramerText35"] = {}
		self._FramerText35 = FramerText(new_state)

	@property
	def FramerText36(self):
		self._getter_access_tracker["FramerText36"] = {}
		return self._FramerText36
	@FramerText36.setter
	def FramerText36(self, new_state):
		self._setter_access_tracker["FramerText36"] = {}
		self._FramerText36 = FramerText(new_state)

	@property
	def FramerText37(self):
		self._getter_access_tracker["FramerText37"] = {}
		return self._FramerText37
	@FramerText37.setter
	def FramerText37(self, new_state):
		self._setter_access_tracker["FramerText37"] = {}
		self._FramerText37 = FramerText(new_state)

	@property
	def FramerText38(self):
		self._getter_access_tracker["FramerText38"] = {}
		return self._FramerText38
	@FramerText38.setter
	def FramerText38(self, new_state):
		self._setter_access_tracker["FramerText38"] = {}
		self._FramerText38 = FramerText(new_state)

	@property
	def FramerText39(self):
		self._getter_access_tracker["FramerText39"] = {}
		return self._FramerText39
	@FramerText39.setter
	def FramerText39(self, new_state):
		self._setter_access_tracker["FramerText39"] = {}
		self._FramerText39 = FramerText(new_state)

	@property
	def FramerText40(self):
		self._getter_access_tracker["FramerText40"] = {}
		return self._FramerText40
	@FramerText40.setter
	def FramerText40(self, new_state):
		self._setter_access_tracker["FramerText40"] = {}
		self._FramerText40 = FramerText(new_state)

	@property
	def FramerText41(self):
		self._getter_access_tracker["FramerText41"] = {}
		return self._FramerText41
	@FramerText41.setter
	def FramerText41(self, new_state):
		self._setter_access_tracker["FramerText41"] = {}
		self._FramerText41 = FramerText(new_state)

	@property
	def FramerText42(self):
		self._getter_access_tracker["FramerText42"] = {}
		return self._FramerText42
	@FramerText42.setter
	def FramerText42(self, new_state):
		self._setter_access_tracker["FramerText42"] = {}
		self._FramerText42 = FramerText(new_state)

	@property
	def Anchor15(self):
		self._getter_access_tracker["Anchor15"] = {}
		return self._Anchor15
	@Anchor15.setter
	def Anchor15(self, new_state):
		self._setter_access_tracker["Anchor15"] = {}
		self._Anchor15 = Anchor(new_state)

	@property
	def Anchor16(self):
		self._getter_access_tracker["Anchor16"] = {}
		return self._Anchor16
	@Anchor16.setter
	def Anchor16(self, new_state):
		self._setter_access_tracker["Anchor16"] = {}
		self._Anchor16 = Anchor(new_state)

	@property
	def Anchor17(self):
		self._getter_access_tracker["Anchor17"] = {}
		return self._Anchor17
	@Anchor17.setter
	def Anchor17(self, new_state):
		self._setter_access_tracker["Anchor17"] = {}
		self._Anchor17 = Anchor(new_state)

	@property
	def Anchor18(self):
		self._getter_access_tracker["Anchor18"] = {}
		return self._Anchor18
	@Anchor18.setter
	def Anchor18(self, new_state):
		self._setter_access_tracker["Anchor18"] = {}
		self._Anchor18 = Anchor(new_state)

	@property
	def Anchor19(self):
		self._getter_access_tracker["Anchor19"] = {}
		return self._Anchor19
	@Anchor19.setter
	def Anchor19(self, new_state):
		self._setter_access_tracker["Anchor19"] = {}
		self._Anchor19 = Anchor(new_state)

	@property
	def Anchor20(self):
		self._getter_access_tracker["Anchor20"] = {}
		return self._Anchor20
	@Anchor20.setter
	def Anchor20(self, new_state):
		self._setter_access_tracker["Anchor20"] = {}
		self._Anchor20 = Anchor(new_state)

	@property
	def Anchor21(self):
		self._getter_access_tracker["Anchor21"] = {}
		return self._Anchor21
	@Anchor21.setter
	def Anchor21(self, new_state):
		self._setter_access_tracker["Anchor21"] = {}
		self._Anchor21 = Anchor(new_state)

	@property
	def Anchor22(self):
		self._getter_access_tracker["Anchor22"] = {}
		return self._Anchor22
	@Anchor22.setter
	def Anchor22(self, new_state):
		self._setter_access_tracker["Anchor22"] = {}
		self._Anchor22 = Anchor(new_state)

	@property
	def Anchor23(self):
		self._getter_access_tracker["Anchor23"] = {}
		return self._Anchor23
	@Anchor23.setter
	def Anchor23(self, new_state):
		self._setter_access_tracker["Anchor23"] = {}
		self._Anchor23 = Anchor(new_state)

	@property
	def Anchor24(self):
		self._getter_access_tracker["Anchor24"] = {}
		return self._Anchor24
	@Anchor24.setter
	def Anchor24(self, new_state):
		self._setter_access_tracker["Anchor24"] = {}
		self._Anchor24 = Anchor(new_state)

	@property
	def Anchor25(self):
		self._getter_access_tracker["Anchor25"] = {}
		return self._Anchor25
	@Anchor25.setter
	def Anchor25(self, new_state):
		self._setter_access_tracker["Anchor25"] = {}
		self._Anchor25 = Anchor(new_state)

	@property
	def Anchor26(self):
		self._getter_access_tracker["Anchor26"] = {}
		return self._Anchor26
	@Anchor26.setter
	def Anchor26(self, new_state):
		self._setter_access_tracker["Anchor26"] = {}
		self._Anchor26 = Anchor(new_state)

	@property
	def Anchor27(self):
		self._getter_access_tracker["Anchor27"] = {}
		return self._Anchor27
	@Anchor27.setter
	def Anchor27(self, new_state):
		self._setter_access_tracker["Anchor27"] = {}
		self._Anchor27 = Anchor(new_state)

	@property
	def Anchor28(self):
		self._getter_access_tracker["Anchor28"] = {}
		return self._Anchor28
	@Anchor28.setter
	def Anchor28(self, new_state):
		self._setter_access_tracker["Anchor28"] = {}
		self._Anchor28 = Anchor(new_state)

	@property
	def Anchor29(self):
		self._getter_access_tracker["Anchor29"] = {}
		return self._Anchor29
	@Anchor29.setter
	def Anchor29(self, new_state):
		self._setter_access_tracker["Anchor29"] = {}
		self._Anchor29 = Anchor(new_state)

	@property
	def Anchor30(self):
		self._getter_access_tracker["Anchor30"] = {}
		return self._Anchor30
	@Anchor30.setter
	def Anchor30(self, new_state):
		self._setter_access_tracker["Anchor30"] = {}
		self._Anchor30 = Anchor(new_state)

	@property
	def Anchor31(self):
		self._getter_access_tracker["Anchor31"] = {}
		return self._Anchor31
	@Anchor31.setter
	def Anchor31(self, new_state):
		self._setter_access_tracker["Anchor31"] = {}
		self._Anchor31 = Anchor(new_state)

	@property
	def Anchor32(self):
		self._getter_access_tracker["Anchor32"] = {}
		return self._Anchor32
	@Anchor32.setter
	def Anchor32(self, new_state):
		self._setter_access_tracker["Anchor32"] = {}
		self._Anchor32 = Anchor(new_state)

	@property
	def Anchor33(self):
		self._getter_access_tracker["Anchor33"] = {}
		return self._Anchor33
	@Anchor33.setter
	def Anchor33(self, new_state):
		self._setter_access_tracker["Anchor33"] = {}
		self._Anchor33 = Anchor(new_state)

	@property
	def Anchor34(self):
		self._getter_access_tracker["Anchor34"] = {}
		return self._Anchor34
	@Anchor34.setter
	def Anchor34(self, new_state):
		self._setter_access_tracker["Anchor34"] = {}
		self._Anchor34 = Anchor(new_state)

	@property
	def Anchor35(self):
		self._getter_access_tracker["Anchor35"] = {}
		return self._Anchor35
	@Anchor35.setter
	def Anchor35(self, new_state):
		self._setter_access_tracker["Anchor35"] = {}
		self._Anchor35 = Anchor(new_state)

	@property
	def Anchor36(self):
		self._getter_access_tracker["Anchor36"] = {}
		return self._Anchor36
	@Anchor36.setter
	def Anchor36(self, new_state):
		self._setter_access_tracker["Anchor36"] = {}
		self._Anchor36 = Anchor(new_state)

	@property
	def Anchor37(self):
		self._getter_access_tracker["Anchor37"] = {}
		return self._Anchor37
	@Anchor37.setter
	def Anchor37(self, new_state):
		self._setter_access_tracker["Anchor37"] = {}
		self._Anchor37 = Anchor(new_state)

	@property
	def Anchor38(self):
		self._getter_access_tracker["Anchor38"] = {}
		return self._Anchor38
	@Anchor38.setter
	def Anchor38(self, new_state):
		self._setter_access_tracker["Anchor38"] = {}
		self._Anchor38 = Anchor(new_state)

	@property
	def Anchor39(self):
		self._getter_access_tracker["Anchor39"] = {}
		return self._Anchor39
	@Anchor39.setter
	def Anchor39(self, new_state):
		self._setter_access_tracker["Anchor39"] = {}
		self._Anchor39 = Anchor(new_state)

	@property
	def Anchor40(self):
		self._getter_access_tracker["Anchor40"] = {}
		return self._Anchor40
	@Anchor40.setter
	def Anchor40(self, new_state):
		self._setter_access_tracker["Anchor40"] = {}
		self._Anchor40 = Anchor(new_state)

	@property
	def Anchor41(self):
		self._getter_access_tracker["Anchor41"] = {}
		return self._Anchor41
	@Anchor41.setter
	def Anchor41(self, new_state):
		self._setter_access_tracker["Anchor41"] = {}
		self._Anchor41 = Anchor(new_state)

	@property
	def Anchor42(self):
		self._getter_access_tracker["Anchor42"] = {}
		return self._Anchor42
	@Anchor42.setter
	def Anchor42(self, new_state):
		self._setter_access_tracker["Anchor42"] = {}
		self._Anchor42 = Anchor(new_state)

	@property
	def Anchor43(self):
		self._getter_access_tracker["Anchor43"] = {}
		return self._Anchor43
	@Anchor43.setter
	def Anchor43(self, new_state):
		self._setter_access_tracker["Anchor43"] = {}
		self._Anchor43 = Anchor(new_state)

	@property
	def Anchor44(self):
		self._getter_access_tracker["Anchor44"] = {}
		return self._Anchor44
	@Anchor44.setter
	def Anchor44(self, new_state):
		self._setter_access_tracker["Anchor44"] = {}
		self._Anchor44 = Anchor(new_state)

	@property
	def Anchor45(self):
		self._getter_access_tracker["Anchor45"] = {}
		return self._Anchor45
	@Anchor45.setter
	def Anchor45(self, new_state):
		self._setter_access_tracker["Anchor45"] = {}
		self._Anchor45 = Anchor(new_state)

	@property
	def Anchor46(self):
		self._getter_access_tracker["Anchor46"] = {}
		return self._Anchor46
	@Anchor46.setter
	def Anchor46(self, new_state):
		self._setter_access_tracker["Anchor46"] = {}
		self._Anchor46 = Anchor(new_state)

	@property
	def Anchor47(self):
		self._getter_access_tracker["Anchor47"] = {}
		return self._Anchor47
	@Anchor47.setter
	def Anchor47(self, new_state):
		self._setter_access_tracker["Anchor47"] = {}
		self._Anchor47 = Anchor(new_state)

	@property
	def Anchor48(self):
		self._getter_access_tracker["Anchor48"] = {}
		return self._Anchor48
	@Anchor48.setter
	def Anchor48(self, new_state):
		self._setter_access_tracker["Anchor48"] = {}
		self._Anchor48 = Anchor(new_state)

	@property
	def Anchor49(self):
		self._getter_access_tracker["Anchor49"] = {}
		return self._Anchor49
	@Anchor49.setter
	def Anchor49(self, new_state):
		self._setter_access_tracker["Anchor49"] = {}
		self._Anchor49 = Anchor(new_state)

	@property
	def Anchor50(self):
		self._getter_access_tracker["Anchor50"] = {}
		return self._Anchor50
	@Anchor50.setter
	def Anchor50(self, new_state):
		self._setter_access_tracker["Anchor50"] = {}
		self._Anchor50 = Anchor(new_state)

	@property
	def Anchor51(self):
		self._getter_access_tracker["Anchor51"] = {}
		return self._Anchor51
	@Anchor51.setter
	def Anchor51(self, new_state):
		self._setter_access_tracker["Anchor51"] = {}
		self._Anchor51 = Anchor(new_state)

	@property
	def Anchor52(self):
		self._getter_access_tracker["Anchor52"] = {}
		return self._Anchor52
	@Anchor52.setter
	def Anchor52(self, new_state):
		self._setter_access_tracker["Anchor52"] = {}
		self._Anchor52 = Anchor(new_state)

	@property
	def Anchor53(self):
		self._getter_access_tracker["Anchor53"] = {}
		return self._Anchor53
	@Anchor53.setter
	def Anchor53(self, new_state):
		self._setter_access_tracker["Anchor53"] = {}
		self._Anchor53 = Anchor(new_state)

	@property
	def Anchor54(self):
		self._getter_access_tracker["Anchor54"] = {}
		return self._Anchor54
	@Anchor54.setter
	def Anchor54(self, new_state):
		self._setter_access_tracker["Anchor54"] = {}
		self._Anchor54 = Anchor(new_state)

	@property
	def Anchor55(self):
		self._getter_access_tracker["Anchor55"] = {}
		return self._Anchor55
	@Anchor55.setter
	def Anchor55(self, new_state):
		self._setter_access_tracker["Anchor55"] = {}
		self._Anchor55 = Anchor(new_state)

	@property
	def Anchor56(self):
		self._getter_access_tracker["Anchor56"] = {}
		return self._Anchor56
	@Anchor56.setter
	def Anchor56(self, new_state):
		self._setter_access_tracker["Anchor56"] = {}
		self._Anchor56 = Anchor(new_state)

	@property
	def Flex16(self):
		self._getter_access_tracker["Flex16"] = {}
		return self._Flex16
	@Flex16.setter
	def Flex16(self, new_state):
		self._setter_access_tracker["Flex16"] = {}
		self._Flex16 = Flex(new_state)

	@property
	def Flex17(self):
		self._getter_access_tracker["Flex17"] = {}
		return self._Flex17
	@Flex17.setter
	def Flex17(self, new_state):
		self._setter_access_tracker["Flex17"] = {}
		self._Flex17 = Flex(new_state)

	@property
	def Image8(self):
		self._getter_access_tracker["Image8"] = {}
		return self._Image8
	@Image8.setter
	def Image8(self, new_state):
		self._setter_access_tracker["Image8"] = {}
		self._Image8 = Image(new_state)

	@property
	def FramerText43(self):
		self._getter_access_tracker["FramerText43"] = {}
		return self._FramerText43
	@FramerText43.setter
	def FramerText43(self, new_state):
		self._setter_access_tracker["FramerText43"] = {}
		self._FramerText43 = FramerText(new_state)

	@property
	def FramerText44(self):
		self._getter_access_tracker["FramerText44"] = {}
		return self._FramerText44
	@FramerText44.setter
	def FramerText44(self, new_state):
		self._setter_access_tracker["FramerText44"] = {}
		self._FramerText44 = FramerText(new_state)

	@property
	def Flex18(self):
		self._getter_access_tracker["Flex18"] = {}
		return self._Flex18
	@Flex18.setter
	def Flex18(self, new_state):
		self._setter_access_tracker["Flex18"] = {}
		self._Flex18 = Flex(new_state)

	@property
	def TextBox19(self):
		self._getter_access_tracker["TextBox19"] = {}
		return self._TextBox19
	@TextBox19.setter
	def TextBox19(self, new_state):
		self._setter_access_tracker["TextBox19"] = {}
		self._TextBox19 = TextBox(new_state)

	@property
	def TextBox20(self):
		self._getter_access_tracker["TextBox20"] = {}
		return self._TextBox20
	@TextBox20.setter
	def TextBox20(self, new_state):
		self._setter_access_tracker["TextBox20"] = {}
		self._TextBox20 = TextBox(new_state)

	@property
	def Flex19(self):
		self._getter_access_tracker["Flex19"] = {}
		return self._Flex19
	@Flex19.setter
	def Flex19(self, new_state):
		self._setter_access_tracker["Flex19"] = {}
		self._Flex19 = Flex(new_state)

	@property
	def TextBox21(self):
		self._getter_access_tracker["TextBox21"] = {}
		return self._TextBox21
	@TextBox21.setter
	def TextBox21(self, new_state):
		self._setter_access_tracker["TextBox21"] = {}
		self._TextBox21 = TextBox(new_state)

	@property
	def Flex20(self):
		self._getter_access_tracker["Flex20"] = {}
		return self._Flex20
	@Flex20.setter
	def Flex20(self, new_state):
		self._setter_access_tracker["Flex20"] = {}
		self._Flex20 = Flex(new_state)

	@property
	def Flex21(self):
		self._getter_access_tracker["Flex21"] = {}
		return self._Flex21
	@Flex21.setter
	def Flex21(self, new_state):
		self._setter_access_tracker["Flex21"] = {}
		self._Flex21 = Flex(new_state)

	@property
	def TextBox22(self):
		self._getter_access_tracker["TextBox22"] = {}
		return self._TextBox22
	@TextBox22.setter
	def TextBox22(self, new_state):
		self._setter_access_tracker["TextBox22"] = {}
		self._TextBox22 = TextBox(new_state)

	@property
	def LineText2(self):
		self._getter_access_tracker["LineText2"] = {}
		return self._LineText2
	@LineText2.setter
	def LineText2(self, new_state):
		self._setter_access_tracker["LineText2"] = {}
		self._LineText2 = LineText(new_state)

	@property
	def LineText3(self):
		self._getter_access_tracker["LineText3"] = {}
		return self._LineText3
	@LineText3.setter
	def LineText3(self, new_state):
		self._setter_access_tracker["LineText3"] = {}
		self._LineText3 = LineText(new_state)

	@property
	def ScaleFlex2(self):
		self._getter_access_tracker["ScaleFlex2"] = {}
		return self._ScaleFlex2
	@ScaleFlex2.setter
	def ScaleFlex2(self, new_state):
		self._setter_access_tracker["ScaleFlex2"] = {}
		self._ScaleFlex2 = ScaleFlex(new_state)

	@property
	def Anchor57(self):
		self._getter_access_tracker["Anchor57"] = {}
		return self._Anchor57
	@Anchor57.setter
	def Anchor57(self, new_state):
		self._setter_access_tracker["Anchor57"] = {}
		self._Anchor57 = Anchor(new_state)

	@property
	def TextBox23(self):
		self._getter_access_tracker["TextBox23"] = {}
		return self._TextBox23
	@TextBox23.setter
	def TextBox23(self, new_state):
		self._setter_access_tracker["TextBox23"] = {}
		self._TextBox23 = TextBox(new_state)

	@property
	def Anchor58(self):
		self._getter_access_tracker["Anchor58"] = {}
		return self._Anchor58
	@Anchor58.setter
	def Anchor58(self, new_state):
		self._setter_access_tracker["Anchor58"] = {}
		self._Anchor58 = Anchor(new_state)

	@property
	def TextBox24(self):
		self._getter_access_tracker["TextBox24"] = {}
		return self._TextBox24
	@TextBox24.setter
	def TextBox24(self, new_state):
		self._setter_access_tracker["TextBox24"] = {}
		self._TextBox24 = TextBox(new_state)

	@property
	def Flex22(self):
		self._getter_access_tracker["Flex22"] = {}
		return self._Flex22
	@Flex22.setter
	def Flex22(self, new_state):
		self._setter_access_tracker["Flex22"] = {}
		self._Flex22 = Flex(new_state)

	@property
	def Flex23(self):
		self._getter_access_tracker["Flex23"] = {}
		return self._Flex23
	@Flex23.setter
	def Flex23(self, new_state):
		self._setter_access_tracker["Flex23"] = {}
		self._Flex23 = Flex(new_state)

	@property
	def Flex24(self):
		self._getter_access_tracker["Flex24"] = {}
		return self._Flex24
	@Flex24.setter
	def Flex24(self, new_state):
		self._setter_access_tracker["Flex24"] = {}
		self._Flex24 = Flex(new_state)

	@property
	def Flex25(self):
		self._getter_access_tracker["Flex25"] = {}
		return self._Flex25
	@Flex25.setter
	def Flex25(self, new_state):
		self._setter_access_tracker["Flex25"] = {}
		self._Flex25 = Flex(new_state)

	@property
	def Anchor59(self):
		self._getter_access_tracker["Anchor59"] = {}
		return self._Anchor59
	@Anchor59.setter
	def Anchor59(self, new_state):
		self._setter_access_tracker["Anchor59"] = {}
		self._Anchor59 = Anchor(new_state)

	@property
	def Anchor60(self):
		self._getter_access_tracker["Anchor60"] = {}
		return self._Anchor60
	@Anchor60.setter
	def Anchor60(self, new_state):
		self._setter_access_tracker["Anchor60"] = {}
		self._Anchor60 = Anchor(new_state)

	@property
	def Anchor61(self):
		self._getter_access_tracker["Anchor61"] = {}
		return self._Anchor61
	@Anchor61.setter
	def Anchor61(self, new_state):
		self._setter_access_tracker["Anchor61"] = {}
		self._Anchor61 = Anchor(new_state)

	@property
	def TextBox25(self):
		self._getter_access_tracker["TextBox25"] = {}
		return self._TextBox25
	@TextBox25.setter
	def TextBox25(self, new_state):
		self._setter_access_tracker["TextBox25"] = {}
		self._TextBox25 = TextBox(new_state)

	@property
	def Flex26(self):
		self._getter_access_tracker["Flex26"] = {}
		return self._Flex26
	@Flex26.setter
	def Flex26(self, new_state):
		self._setter_access_tracker["Flex26"] = {}
		self._Flex26 = Flex(new_state)

	@property
	def Div1(self):
		self._getter_access_tracker["Div1"] = {}
		return self._Div1
	@Div1.setter
	def Div1(self, new_state):
		self._setter_access_tracker["Div1"] = {}
		self._Div1 = Div(new_state)

	@property
	def Flex27(self):
		self._getter_access_tracker["Flex27"] = {}
		return self._Flex27
	@Flex27.setter
	def Flex27(self, new_state):
		self._setter_access_tracker["Flex27"] = {}
		self._Flex27 = Flex(new_state)

	@property
	def Flex28(self):
		self._getter_access_tracker["Flex28"] = {}
		return self._Flex28
	@Flex28.setter
	def Flex28(self, new_state):
		self._setter_access_tracker["Flex28"] = {}
		self._Flex28 = Flex(new_state)

	@property
	def Flex29(self):
		self._getter_access_tracker["Flex29"] = {}
		return self._Flex29
	@Flex29.setter
	def Flex29(self, new_state):
		self._setter_access_tracker["Flex29"] = {}
		self._Flex29 = Flex(new_state)

	@property
	def Flex30(self):
		self._getter_access_tracker["Flex30"] = {}
		return self._Flex30
	@Flex30.setter
	def Flex30(self, new_state):
		self._setter_access_tracker["Flex30"] = {}
		self._Flex30 = Flex(new_state)

	@property
	def Flex31(self):
		self._getter_access_tracker["Flex31"] = {}
		return self._Flex31
	@Flex31.setter
	def Flex31(self, new_state):
		self._setter_access_tracker["Flex31"] = {}
		self._Flex31 = Flex(new_state)

	@property
	def Flex32(self):
		self._getter_access_tracker["Flex32"] = {}
		return self._Flex32
	@Flex32.setter
	def Flex32(self, new_state):
		self._setter_access_tracker["Flex32"] = {}
		self._Flex32 = Flex(new_state)

	@property
	def Div2(self):
		self._getter_access_tracker["Div2"] = {}
		return self._Div2
	@Div2.setter
	def Div2(self, new_state):
		self._setter_access_tracker["Div2"] = {}
		self._Div2 = Div(new_state)

	@property
	def FramerFlex2(self):
		self._getter_access_tracker["FramerFlex2"] = {}
		return self._FramerFlex2
	@FramerFlex2.setter
	def FramerFlex2(self, new_state):
		self._setter_access_tracker["FramerFlex2"] = {}
		self._FramerFlex2 = FramerFlex(new_state)

	@property
	def Flex33(self):
		self._getter_access_tracker["Flex33"] = {}
		return self._Flex33
	@Flex33.setter
	def Flex33(self, new_state):
		self._setter_access_tracker["Flex33"] = {}
		self._Flex33 = Flex(new_state)

	@property
	def footer1(self):
		self._getter_access_tracker["footer1"] = {}
		return self._footer1
	@footer1.setter
	def footer1(self, new_state):
		self._setter_access_tracker["footer1"] = {}
		self._footer1 = Flex(new_state)

	@property
	def TextBox26(self):
		self._getter_access_tracker["TextBox26"] = {}
		return self._TextBox26
	@TextBox26.setter
	def TextBox26(self, new_state):
		self._setter_access_tracker["TextBox26"] = {}
		self._TextBox26 = TextBox(new_state)

	@property
	def TextBox27(self):
		self._getter_access_tracker["TextBox27"] = {}
		return self._TextBox27
	@TextBox27.setter
	def TextBox27(self, new_state):
		self._setter_access_tracker["TextBox27"] = {}
		self._TextBox27 = TextBox(new_state)

	@property
	def Flex35(self):
		self._getter_access_tracker["Flex35"] = {}
		return self._Flex35
	@Flex35.setter
	def Flex35(self, new_state):
		self._setter_access_tracker["Flex35"] = {}
		self._Flex35 = Flex(new_state)

	@property
	def FramerFlex3(self):
		self._getter_access_tracker["FramerFlex3"] = {}
		return self._FramerFlex3
	@FramerFlex3.setter
	def FramerFlex3(self, new_state):
		self._setter_access_tracker["FramerFlex3"] = {}
		self._FramerFlex3 = FramerFlex(new_state)

	@property
	def Flex36(self):
		self._getter_access_tracker["Flex36"] = {}
		return self._Flex36
	@Flex36.setter
	def Flex36(self, new_state):
		self._setter_access_tracker["Flex36"] = {}
		self._Flex36 = Flex(new_state)

	@property
	def Flex37(self):
		self._getter_access_tracker["Flex37"] = {}
		return self._Flex37
	@Flex37.setter
	def Flex37(self, new_state):
		self._setter_access_tracker["Flex37"] = {}
		self._Flex37 = Flex(new_state)

	@property
	def Flex38(self):
		self._getter_access_tracker["Flex38"] = {}
		return self._Flex38
	@Flex38.setter
	def Flex38(self, new_state):
		self._setter_access_tracker["Flex38"] = {}
		self._Flex38 = Flex(new_state)

	@property
	def FramerFlex4(self):
		self._getter_access_tracker["FramerFlex4"] = {}
		return self._FramerFlex4
	@FramerFlex4.setter
	def FramerFlex4(self, new_state):
		self._setter_access_tracker["FramerFlex4"] = {}
		self._FramerFlex4 = FramerFlex(new_state)

	@property
	def Div3(self):
		self._getter_access_tracker["Div3"] = {}
		return self._Div3
	@Div3.setter
	def Div3(self, new_state):
		self._setter_access_tracker["Div3"] = {}
		self._Div3 = Div(new_state)

	@property
	def Flex40(self):
		self._getter_access_tracker["Flex40"] = {}
		return self._Flex40
	@Flex40.setter
	def Flex40(self, new_state):
		self._setter_access_tracker["Flex40"] = {}
		self._Flex40 = Flex(new_state)

	@property
	def TextBox28(self):
		self._getter_access_tracker["TextBox28"] = {}
		return self._TextBox28
	@TextBox28.setter
	def TextBox28(self, new_state):
		self._setter_access_tracker["TextBox28"] = {}
		self._TextBox28 = TextBox(new_state)

	@property
	def TextBox29(self):
		self._getter_access_tracker["TextBox29"] = {}
		return self._TextBox29
	@TextBox29.setter
	def TextBox29(self, new_state):
		self._setter_access_tracker["TextBox29"] = {}
		self._TextBox29 = TextBox(new_state)

	@property
	def Flex47(self):
		self._getter_access_tracker["Flex47"] = {}
		return self._Flex47
	@Flex47.setter
	def Flex47(self, new_state):
		self._setter_access_tracker["Flex47"] = {}
		self._Flex47 = Flex(new_state)

	@property
	def Flex48(self):
		self._getter_access_tracker["Flex48"] = {}
		return self._Flex48
	@Flex48.setter
	def Flex48(self, new_state):
		self._setter_access_tracker["Flex48"] = {}
		self._Flex48 = Flex(new_state)

	@property
	def Flex49(self):
		self._getter_access_tracker["Flex49"] = {}
		return self._Flex49
	@Flex49.setter
	def Flex49(self, new_state):
		self._setter_access_tracker["Flex49"] = {}
		self._Flex49 = Flex(new_state)

	@property
	def FramerFlex9(self):
		self._getter_access_tracker["FramerFlex9"] = {}
		return self._FramerFlex9
	@FramerFlex9.setter
	def FramerFlex9(self, new_state):
		self._setter_access_tracker["FramerFlex9"] = {}
		self._FramerFlex9 = FramerFlex(new_state)

	@property
	def TextBox38(self):
		self._getter_access_tracker["TextBox38"] = {}
		return self._TextBox38
	@TextBox38.setter
	def TextBox38(self, new_state):
		self._setter_access_tracker["TextBox38"] = {}
		self._TextBox38 = TextBox(new_state)

	@property
	def TextBox39(self):
		self._getter_access_tracker["TextBox39"] = {}
		return self._TextBox39
	@TextBox39.setter
	def TextBox39(self, new_state):
		self._setter_access_tracker["TextBox39"] = {}
		self._TextBox39 = TextBox(new_state)

	@property
	def Flex50(self):
		self._getter_access_tracker["Flex50"] = {}
		return self._Flex50
	@Flex50.setter
	def Flex50(self, new_state):
		self._setter_access_tracker["Flex50"] = {}
		self._Flex50 = Flex(new_state)

	@property
	def Div8(self):
		self._getter_access_tracker["Div8"] = {}
		return self._Div8
	@Div8.setter
	def Div8(self, new_state):
		self._setter_access_tracker["Div8"] = {}
		self._Div8 = Div(new_state)

	@property
	def TextBox40(self):
		self._getter_access_tracker["TextBox40"] = {}
		return self._TextBox40
	@TextBox40.setter
	def TextBox40(self, new_state):
		self._setter_access_tracker["TextBox40"] = {}
		self._TextBox40 = TextBox(new_state)

	@property
	def TextBox41(self):
		self._getter_access_tracker["TextBox41"] = {}
		return self._TextBox41
	@TextBox41.setter
	def TextBox41(self, new_state):
		self._setter_access_tracker["TextBox41"] = {}
		self._TextBox41 = TextBox(new_state)

	@property
	def Div9(self):
		self._getter_access_tracker["Div9"] = {}
		return self._Div9
	@Div9.setter
	def Div9(self, new_state):
		self._setter_access_tracker["Div9"] = {}
		self._Div9 = Div(new_state)

	@property
	def Flex51(self):
		self._getter_access_tracker["Flex51"] = {}
		return self._Flex51
	@Flex51.setter
	def Flex51(self, new_state):
		self._setter_access_tracker["Flex51"] = {}
		self._Flex51 = Flex(new_state)

	@property
	def FramerFlex10(self):
		self._getter_access_tracker["FramerFlex10"] = {}
		return self._FramerFlex10
	@FramerFlex10.setter
	def FramerFlex10(self, new_state):
		self._setter_access_tracker["FramerFlex10"] = {}
		self._FramerFlex10 = FramerFlex(new_state)

	@property
	def TextBox42(self):
		self._getter_access_tracker["TextBox42"] = {}
		return self._TextBox42
	@TextBox42.setter
	def TextBox42(self, new_state):
		self._setter_access_tracker["TextBox42"] = {}
		self._TextBox42 = TextBox(new_state)

	@property
	def TextBox43(self):
		self._getter_access_tracker["TextBox43"] = {}
		return self._TextBox43
	@TextBox43.setter
	def TextBox43(self, new_state):
		self._setter_access_tracker["TextBox43"] = {}
		self._TextBox43 = TextBox(new_state)

	@property
	def Div10(self):
		self._getter_access_tracker["Div10"] = {}
		return self._Div10
	@Div10.setter
	def Div10(self, new_state):
		self._setter_access_tracker["Div10"] = {}
		self._Div10 = Div(new_state)

	@property
	def Flex52(self):
		self._getter_access_tracker["Flex52"] = {}
		return self._Flex52
	@Flex52.setter
	def Flex52(self, new_state):
		self._setter_access_tracker["Flex52"] = {}
		self._Flex52 = Flex(new_state)

	@property
	def FramerFlex11(self):
		self._getter_access_tracker["FramerFlex11"] = {}
		return self._FramerFlex11
	@FramerFlex11.setter
	def FramerFlex11(self, new_state):
		self._setter_access_tracker["FramerFlex11"] = {}
		self._FramerFlex11 = FramerFlex(new_state)

	@property
	def TextBox45(self):
		self._getter_access_tracker["TextBox45"] = {}
		return self._TextBox45
	@TextBox45.setter
	def TextBox45(self, new_state):
		self._setter_access_tracker["TextBox45"] = {}
		self._TextBox45 = TextBox(new_state)

	@property
	def Div11(self):
		self._getter_access_tracker["Div11"] = {}
		return self._Div11
	@Div11.setter
	def Div11(self, new_state):
		self._setter_access_tracker["Div11"] = {}
		self._Div11 = Div(new_state)

	@property
	def Flex53(self):
		self._getter_access_tracker["Flex53"] = {}
		return self._Flex53
	@Flex53.setter
	def Flex53(self, new_state):
		self._setter_access_tracker["Flex53"] = {}
		self._Flex53 = Flex(new_state)

	@property
	def FramerFlex12(self):
		self._getter_access_tracker["FramerFlex12"] = {}
		return self._FramerFlex12
	@FramerFlex12.setter
	def FramerFlex12(self, new_state):
		self._setter_access_tracker["FramerFlex12"] = {}
		self._FramerFlex12 = FramerFlex(new_state)

	@property
	def Image10(self):
		self._getter_access_tracker["Image10"] = {}
		return self._Image10
	@Image10.setter
	def Image10(self, new_state):
		self._setter_access_tracker["Image10"] = {}
		self._Image10 = Image(new_state)

	@property
	def Flex54(self):
		self._getter_access_tracker["Flex54"] = {}
		return self._Flex54
	@Flex54.setter
	def Flex54(self, new_state):
		self._setter_access_tracker["Flex54"] = {}
		self._Flex54 = Flex(new_state)

	@property
	def Flex55(self):
		self._getter_access_tracker["Flex55"] = {}
		return self._Flex55
	@Flex55.setter
	def Flex55(self, new_state):
		self._setter_access_tracker["Flex55"] = {}
		self._Flex55 = Flex(new_state)

	@property
	def FramerFlex13(self):
		self._getter_access_tracker["FramerFlex13"] = {}
		return self._FramerFlex13
	@FramerFlex13.setter
	def FramerFlex13(self, new_state):
		self._setter_access_tracker["FramerFlex13"] = {}
		self._FramerFlex13 = FramerFlex(new_state)

	@property
	def Flex56(self):
		self._getter_access_tracker["Flex56"] = {}
		return self._Flex56
	@Flex56.setter
	def Flex56(self, new_state):
		self._setter_access_tracker["Flex56"] = {}
		self._Flex56 = Flex(new_state)

	@property
	def Div12(self):
		self._getter_access_tracker["Div12"] = {}
		return self._Div12
	@Div12.setter
	def Div12(self, new_state):
		self._setter_access_tracker["Div12"] = {}
		self._Div12 = Div(new_state)

	@property
	def TextBox46(self):
		self._getter_access_tracker["TextBox46"] = {}
		return self._TextBox46
	@TextBox46.setter
	def TextBox46(self, new_state):
		self._setter_access_tracker["TextBox46"] = {}
		self._TextBox46 = TextBox(new_state)

	@property
	def Flex57(self):
		self._getter_access_tracker["Flex57"] = {}
		return self._Flex57
	@Flex57.setter
	def Flex57(self, new_state):
		self._setter_access_tracker["Flex57"] = {}
		self._Flex57 = Flex(new_state)

	@property
	def FramerFlex14(self):
		self._getter_access_tracker["FramerFlex14"] = {}
		return self._FramerFlex14
	@FramerFlex14.setter
	def FramerFlex14(self, new_state):
		self._setter_access_tracker["FramerFlex14"] = {}
		self._FramerFlex14 = FramerFlex(new_state)

	@property
	def Anchor62(self):
		self._getter_access_tracker["Anchor62"] = {}
		return self._Anchor62
	@Anchor62.setter
	def Anchor62(self, new_state):
		self._setter_access_tracker["Anchor62"] = {}
		self._Anchor62 = Anchor(new_state)

	@property
	def ScaleFlex3(self):
		self._getter_access_tracker["ScaleFlex3"] = {}
		return self._ScaleFlex3
	@ScaleFlex3.setter
	def ScaleFlex3(self, new_state):
		self._setter_access_tracker["ScaleFlex3"] = {}
		self._ScaleFlex3 = ScaleFlex(new_state)

	@property
	def Image11(self):
		self._getter_access_tracker["Image11"] = {}
		return self._Image11
	@Image11.setter
	def Image11(self, new_state):
		self._setter_access_tracker["Image11"] = {}
		self._Image11 = Image(new_state)

	@property
	def TextBox47(self):
		self._getter_access_tracker["TextBox47"] = {}
		return self._TextBox47
	@TextBox47.setter
	def TextBox47(self, new_state):
		self._setter_access_tracker["TextBox47"] = {}
		self._TextBox47 = TextBox(new_state)

	@property
	def TextBox48(self):
		self._getter_access_tracker["TextBox48"] = {}
		return self._TextBox48
	@TextBox48.setter
	def TextBox48(self, new_state):
		self._setter_access_tracker["TextBox48"] = {}
		self._TextBox48 = TextBox(new_state)

	@property
	def Image12(self):
		self._getter_access_tracker["Image12"] = {}
		return self._Image12
	@Image12.setter
	def Image12(self, new_state):
		self._setter_access_tracker["Image12"] = {}
		self._Image12 = Image(new_state)

	@property
	def ScaleFlex4(self):
		self._getter_access_tracker["ScaleFlex4"] = {}
		return self._ScaleFlex4
	@ScaleFlex4.setter
	def ScaleFlex4(self, new_state):
		self._setter_access_tracker["ScaleFlex4"] = {}
		self._ScaleFlex4 = ScaleFlex(new_state)

	@property
	def Anchor63(self):
		self._getter_access_tracker["Anchor63"] = {}
		return self._Anchor63
	@Anchor63.setter
	def Anchor63(self, new_state):
		self._setter_access_tracker["Anchor63"] = {}
		self._Anchor63 = Anchor(new_state)

	@property
	def FramerFlex15(self):
		self._getter_access_tracker["FramerFlex15"] = {}
		return self._FramerFlex15
	@FramerFlex15.setter
	def FramerFlex15(self, new_state):
		self._setter_access_tracker["FramerFlex15"] = {}
		self._FramerFlex15 = FramerFlex(new_state)

	@property
	def Image13(self):
		self._getter_access_tracker["Image13"] = {}
		return self._Image13
	@Image13.setter
	def Image13(self, new_state):
		self._setter_access_tracker["Image13"] = {}
		self._Image13 = Image(new_state)

	@property
	def TextBox49(self):
		self._getter_access_tracker["TextBox49"] = {}
		return self._TextBox49
	@TextBox49.setter
	def TextBox49(self, new_state):
		self._setter_access_tracker["TextBox49"] = {}
		self._TextBox49 = TextBox(new_state)

	@property
	def TextBox50(self):
		self._getter_access_tracker["TextBox50"] = {}
		return self._TextBox50
	@TextBox50.setter
	def TextBox50(self, new_state):
		self._setter_access_tracker["TextBox50"] = {}
		self._TextBox50 = TextBox(new_state)

	@property
	def Image14(self):
		self._getter_access_tracker["Image14"] = {}
		return self._Image14
	@Image14.setter
	def Image14(self, new_state):
		self._setter_access_tracker["Image14"] = {}
		self._Image14 = Image(new_state)

	@property
	def ScaleFlex5(self):
		self._getter_access_tracker["ScaleFlex5"] = {}
		return self._ScaleFlex5
	@ScaleFlex5.setter
	def ScaleFlex5(self, new_state):
		self._setter_access_tracker["ScaleFlex5"] = {}
		self._ScaleFlex5 = ScaleFlex(new_state)

	@property
	def ScaleFlex6(self):
		self._getter_access_tracker["ScaleFlex6"] = {}
		return self._ScaleFlex6
	@ScaleFlex6.setter
	def ScaleFlex6(self, new_state):
		self._setter_access_tracker["ScaleFlex6"] = {}
		self._ScaleFlex6 = ScaleFlex(new_state)

	@property
	def Anchor64(self):
		self._getter_access_tracker["Anchor64"] = {}
		return self._Anchor64
	@Anchor64.setter
	def Anchor64(self, new_state):
		self._setter_access_tracker["Anchor64"] = {}
		self._Anchor64 = Anchor(new_state)

	@property
	def Anchor65(self):
		self._getter_access_tracker["Anchor65"] = {}
		return self._Anchor65
	@Anchor65.setter
	def Anchor65(self, new_state):
		self._setter_access_tracker["Anchor65"] = {}
		self._Anchor65 = Anchor(new_state)

	@property
	def FramerFlex16(self):
		self._getter_access_tracker["FramerFlex16"] = {}
		return self._FramerFlex16
	@FramerFlex16.setter
	def FramerFlex16(self, new_state):
		self._setter_access_tracker["FramerFlex16"] = {}
		self._FramerFlex16 = FramerFlex(new_state)

	@property
	def FramerFlex17(self):
		self._getter_access_tracker["FramerFlex17"] = {}
		return self._FramerFlex17
	@FramerFlex17.setter
	def FramerFlex17(self, new_state):
		self._setter_access_tracker["FramerFlex17"] = {}
		self._FramerFlex17 = FramerFlex(new_state)

	@property
	def Flex58(self):
		self._getter_access_tracker["Flex58"] = {}
		return self._Flex58
	@Flex58.setter
	def Flex58(self, new_state):
		self._setter_access_tracker["Flex58"] = {}
		self._Flex58 = Flex(new_state)

	@property
	def Image15(self):
		self._getter_access_tracker["Image15"] = {}
		return self._Image15
	@Image15.setter
	def Image15(self, new_state):
		self._setter_access_tracker["Image15"] = {}
		self._Image15 = Image(new_state)

	@property
	def TextBox51(self):
		self._getter_access_tracker["TextBox51"] = {}
		return self._TextBox51
	@TextBox51.setter
	def TextBox51(self, new_state):
		self._setter_access_tracker["TextBox51"] = {}
		self._TextBox51 = TextBox(new_state)

	@property
	def TextBox52(self):
		self._getter_access_tracker["TextBox52"] = {}
		return self._TextBox52
	@TextBox52.setter
	def TextBox52(self, new_state):
		self._setter_access_tracker["TextBox52"] = {}
		self._TextBox52 = TextBox(new_state)

	@property
	def Image16(self):
		self._getter_access_tracker["Image16"] = {}
		return self._Image16
	@Image16.setter
	def Image16(self, new_state):
		self._setter_access_tracker["Image16"] = {}
		self._Image16 = Image(new_state)

	@property
	def ScaleFlex7(self):
		self._getter_access_tracker["ScaleFlex7"] = {}
		return self._ScaleFlex7
	@ScaleFlex7.setter
	def ScaleFlex7(self, new_state):
		self._setter_access_tracker["ScaleFlex7"] = {}
		self._ScaleFlex7 = ScaleFlex(new_state)

	@property
	def ScaleFlex8(self):
		self._getter_access_tracker["ScaleFlex8"] = {}
		return self._ScaleFlex8
	@ScaleFlex8.setter
	def ScaleFlex8(self, new_state):
		self._setter_access_tracker["ScaleFlex8"] = {}
		self._ScaleFlex8 = ScaleFlex(new_state)

	@property
	def Anchor66(self):
		self._getter_access_tracker["Anchor66"] = {}
		return self._Anchor66
	@Anchor66.setter
	def Anchor66(self, new_state):
		self._setter_access_tracker["Anchor66"] = {}
		self._Anchor66 = Anchor(new_state)

	@property
	def Anchor67(self):
		self._getter_access_tracker["Anchor67"] = {}
		return self._Anchor67
	@Anchor67.setter
	def Anchor67(self, new_state):
		self._setter_access_tracker["Anchor67"] = {}
		self._Anchor67 = Anchor(new_state)

	@property
	def FramerFlex18(self):
		self._getter_access_tracker["FramerFlex18"] = {}
		return self._FramerFlex18
	@FramerFlex18.setter
	def FramerFlex18(self, new_state):
		self._setter_access_tracker["FramerFlex18"] = {}
		self._FramerFlex18 = FramerFlex(new_state)

	@property
	def FramerFlex19(self):
		self._getter_access_tracker["FramerFlex19"] = {}
		return self._FramerFlex19
	@FramerFlex19.setter
	def FramerFlex19(self, new_state):
		self._setter_access_tracker["FramerFlex19"] = {}
		self._FramerFlex19 = FramerFlex(new_state)

	@property
	def Flex59(self):
		self._getter_access_tracker["Flex59"] = {}
		return self._Flex59
	@Flex59.setter
	def Flex59(self, new_state):
		self._setter_access_tracker["Flex59"] = {}
		self._Flex59 = Flex(new_state)

	@property
	def Image17(self):
		self._getter_access_tracker["Image17"] = {}
		return self._Image17
	@Image17.setter
	def Image17(self, new_state):
		self._setter_access_tracker["Image17"] = {}
		self._Image17 = Image(new_state)

	@property
	def TextBox53(self):
		self._getter_access_tracker["TextBox53"] = {}
		return self._TextBox53
	@TextBox53.setter
	def TextBox53(self, new_state):
		self._setter_access_tracker["TextBox53"] = {}
		self._TextBox53 = TextBox(new_state)

	@property
	def TextBox54(self):
		self._getter_access_tracker["TextBox54"] = {}
		return self._TextBox54
	@TextBox54.setter
	def TextBox54(self, new_state):
		self._setter_access_tracker["TextBox54"] = {}
		self._TextBox54 = TextBox(new_state)

	@property
	def Image18(self):
		self._getter_access_tracker["Image18"] = {}
		return self._Image18
	@Image18.setter
	def Image18(self, new_state):
		self._setter_access_tracker["Image18"] = {}
		self._Image18 = Image(new_state)

	@property
	def ScaleFlex9(self):
		self._getter_access_tracker["ScaleFlex9"] = {}
		return self._ScaleFlex9
	@ScaleFlex9.setter
	def ScaleFlex9(self, new_state):
		self._setter_access_tracker["ScaleFlex9"] = {}
		self._ScaleFlex9 = ScaleFlex(new_state)

	@property
	def ScaleFlex10(self):
		self._getter_access_tracker["ScaleFlex10"] = {}
		return self._ScaleFlex10
	@ScaleFlex10.setter
	def ScaleFlex10(self, new_state):
		self._setter_access_tracker["ScaleFlex10"] = {}
		self._ScaleFlex10 = ScaleFlex(new_state)

	@property
	def Anchor68(self):
		self._getter_access_tracker["Anchor68"] = {}
		return self._Anchor68
	@Anchor68.setter
	def Anchor68(self, new_state):
		self._setter_access_tracker["Anchor68"] = {}
		self._Anchor68 = Anchor(new_state)

	@property
	def Anchor69(self):
		self._getter_access_tracker["Anchor69"] = {}
		return self._Anchor69
	@Anchor69.setter
	def Anchor69(self, new_state):
		self._setter_access_tracker["Anchor69"] = {}
		self._Anchor69 = Anchor(new_state)

	@property
	def FramerFlex20(self):
		self._getter_access_tracker["FramerFlex20"] = {}
		return self._FramerFlex20
	@FramerFlex20.setter
	def FramerFlex20(self, new_state):
		self._setter_access_tracker["FramerFlex20"] = {}
		self._FramerFlex20 = FramerFlex(new_state)

	@property
	def FramerFlex21(self):
		self._getter_access_tracker["FramerFlex21"] = {}
		return self._FramerFlex21
	@FramerFlex21.setter
	def FramerFlex21(self, new_state):
		self._setter_access_tracker["FramerFlex21"] = {}
		self._FramerFlex21 = FramerFlex(new_state)

	@property
	def Flex60(self):
		self._getter_access_tracker["Flex60"] = {}
		return self._Flex60
	@Flex60.setter
	def Flex60(self, new_state):
		self._setter_access_tracker["Flex60"] = {}
		self._Flex60 = Flex(new_state)

	@property
	def Image19(self):
		self._getter_access_tracker["Image19"] = {}
		return self._Image19
	@Image19.setter
	def Image19(self, new_state):
		self._setter_access_tracker["Image19"] = {}
		self._Image19 = Image(new_state)

	@property
	def TextBox55(self):
		self._getter_access_tracker["TextBox55"] = {}
		return self._TextBox55
	@TextBox55.setter
	def TextBox55(self, new_state):
		self._setter_access_tracker["TextBox55"] = {}
		self._TextBox55 = TextBox(new_state)

	@property
	def TextBox56(self):
		self._getter_access_tracker["TextBox56"] = {}
		return self._TextBox56
	@TextBox56.setter
	def TextBox56(self, new_state):
		self._setter_access_tracker["TextBox56"] = {}
		self._TextBox56 = TextBox(new_state)

	@property
	def Image20(self):
		self._getter_access_tracker["Image20"] = {}
		return self._Image20
	@Image20.setter
	def Image20(self, new_state):
		self._setter_access_tracker["Image20"] = {}
		self._Image20 = Image(new_state)

	@property
	def ScaleFlex11(self):
		self._getter_access_tracker["ScaleFlex11"] = {}
		return self._ScaleFlex11
	@ScaleFlex11.setter
	def ScaleFlex11(self, new_state):
		self._setter_access_tracker["ScaleFlex11"] = {}
		self._ScaleFlex11 = ScaleFlex(new_state)

	@property
	def ScaleFlex12(self):
		self._getter_access_tracker["ScaleFlex12"] = {}
		return self._ScaleFlex12
	@ScaleFlex12.setter
	def ScaleFlex12(self, new_state):
		self._setter_access_tracker["ScaleFlex12"] = {}
		self._ScaleFlex12 = ScaleFlex(new_state)

	@property
	def Anchor70(self):
		self._getter_access_tracker["Anchor70"] = {}
		return self._Anchor70
	@Anchor70.setter
	def Anchor70(self, new_state):
		self._setter_access_tracker["Anchor70"] = {}
		self._Anchor70 = Anchor(new_state)

	@property
	def Anchor71(self):
		self._getter_access_tracker["Anchor71"] = {}
		return self._Anchor71
	@Anchor71.setter
	def Anchor71(self, new_state):
		self._setter_access_tracker["Anchor71"] = {}
		self._Anchor71 = Anchor(new_state)

	@property
	def FramerFlex22(self):
		self._getter_access_tracker["FramerFlex22"] = {}
		return self._FramerFlex22
	@FramerFlex22.setter
	def FramerFlex22(self, new_state):
		self._setter_access_tracker["FramerFlex22"] = {}
		self._FramerFlex22 = FramerFlex(new_state)

	@property
	def FramerFlex23(self):
		self._getter_access_tracker["FramerFlex23"] = {}
		return self._FramerFlex23
	@FramerFlex23.setter
	def FramerFlex23(self, new_state):
		self._setter_access_tracker["FramerFlex23"] = {}
		self._FramerFlex23 = FramerFlex(new_state)

	@property
	def Flex61(self):
		self._getter_access_tracker["Flex61"] = {}
		return self._Flex61
	@Flex61.setter
	def Flex61(self, new_state):
		self._setter_access_tracker["Flex61"] = {}
		self._Flex61 = Flex(new_state)

	@property
	def Image21(self):
		self._getter_access_tracker["Image21"] = {}
		return self._Image21
	@Image21.setter
	def Image21(self, new_state):
		self._setter_access_tracker["Image21"] = {}
		self._Image21 = Image(new_state)

	@property
	def TextBox57(self):
		self._getter_access_tracker["TextBox57"] = {}
		return self._TextBox57
	@TextBox57.setter
	def TextBox57(self, new_state):
		self._setter_access_tracker["TextBox57"] = {}
		self._TextBox57 = TextBox(new_state)

	@property
	def TextBox58(self):
		self._getter_access_tracker["TextBox58"] = {}
		return self._TextBox58
	@TextBox58.setter
	def TextBox58(self, new_state):
		self._setter_access_tracker["TextBox58"] = {}
		self._TextBox58 = TextBox(new_state)

	@property
	def Image22(self):
		self._getter_access_tracker["Image22"] = {}
		return self._Image22
	@Image22.setter
	def Image22(self, new_state):
		self._setter_access_tracker["Image22"] = {}
		self._Image22 = Image(new_state)

	@property
	def ScaleFlex13(self):
		self._getter_access_tracker["ScaleFlex13"] = {}
		return self._ScaleFlex13
	@ScaleFlex13.setter
	def ScaleFlex13(self, new_state):
		self._setter_access_tracker["ScaleFlex13"] = {}
		self._ScaleFlex13 = ScaleFlex(new_state)

	@property
	def ScaleFlex14(self):
		self._getter_access_tracker["ScaleFlex14"] = {}
		return self._ScaleFlex14
	@ScaleFlex14.setter
	def ScaleFlex14(self, new_state):
		self._setter_access_tracker["ScaleFlex14"] = {}
		self._ScaleFlex14 = ScaleFlex(new_state)

	@property
	def Anchor72(self):
		self._getter_access_tracker["Anchor72"] = {}
		return self._Anchor72
	@Anchor72.setter
	def Anchor72(self, new_state):
		self._setter_access_tracker["Anchor72"] = {}
		self._Anchor72 = Anchor(new_state)

	@property
	def Anchor73(self):
		self._getter_access_tracker["Anchor73"] = {}
		return self._Anchor73
	@Anchor73.setter
	def Anchor73(self, new_state):
		self._setter_access_tracker["Anchor73"] = {}
		self._Anchor73 = Anchor(new_state)

	@property
	def FramerFlex24(self):
		self._getter_access_tracker["FramerFlex24"] = {}
		return self._FramerFlex24
	@FramerFlex24.setter
	def FramerFlex24(self, new_state):
		self._setter_access_tracker["FramerFlex24"] = {}
		self._FramerFlex24 = FramerFlex(new_state)

	@property
	def FramerFlex25(self):
		self._getter_access_tracker["FramerFlex25"] = {}
		return self._FramerFlex25
	@FramerFlex25.setter
	def FramerFlex25(self, new_state):
		self._setter_access_tracker["FramerFlex25"] = {}
		self._FramerFlex25 = FramerFlex(new_state)

	@property
	def Flex62(self):
		self._getter_access_tracker["Flex62"] = {}
		return self._Flex62
	@Flex62.setter
	def Flex62(self, new_state):
		self._setter_access_tracker["Flex62"] = {}
		self._Flex62 = Flex(new_state)

	@property
	def Image23(self):
		self._getter_access_tracker["Image23"] = {}
		return self._Image23
	@Image23.setter
	def Image23(self, new_state):
		self._setter_access_tracker["Image23"] = {}
		self._Image23 = Image(new_state)

	@property
	def TextBox59(self):
		self._getter_access_tracker["TextBox59"] = {}
		return self._TextBox59
	@TextBox59.setter
	def TextBox59(self, new_state):
		self._setter_access_tracker["TextBox59"] = {}
		self._TextBox59 = TextBox(new_state)

	@property
	def TextBox60(self):
		self._getter_access_tracker["TextBox60"] = {}
		return self._TextBox60
	@TextBox60.setter
	def TextBox60(self, new_state):
		self._setter_access_tracker["TextBox60"] = {}
		self._TextBox60 = TextBox(new_state)

	@property
	def Image24(self):
		self._getter_access_tracker["Image24"] = {}
		return self._Image24
	@Image24.setter
	def Image24(self, new_state):
		self._setter_access_tracker["Image24"] = {}
		self._Image24 = Image(new_state)

	@property
	def ScaleFlex15(self):
		self._getter_access_tracker["ScaleFlex15"] = {}
		return self._ScaleFlex15
	@ScaleFlex15.setter
	def ScaleFlex15(self, new_state):
		self._setter_access_tracker["ScaleFlex15"] = {}
		self._ScaleFlex15 = ScaleFlex(new_state)

	@property
	def ScaleFlex16(self):
		self._getter_access_tracker["ScaleFlex16"] = {}
		return self._ScaleFlex16
	@ScaleFlex16.setter
	def ScaleFlex16(self, new_state):
		self._setter_access_tracker["ScaleFlex16"] = {}
		self._ScaleFlex16 = ScaleFlex(new_state)

	@property
	def Anchor74(self):
		self._getter_access_tracker["Anchor74"] = {}
		return self._Anchor74
	@Anchor74.setter
	def Anchor74(self, new_state):
		self._setter_access_tracker["Anchor74"] = {}
		self._Anchor74 = Anchor(new_state)

	@property
	def Anchor75(self):
		self._getter_access_tracker["Anchor75"] = {}
		return self._Anchor75
	@Anchor75.setter
	def Anchor75(self, new_state):
		self._setter_access_tracker["Anchor75"] = {}
		self._Anchor75 = Anchor(new_state)

	@property
	def FramerFlex26(self):
		self._getter_access_tracker["FramerFlex26"] = {}
		return self._FramerFlex26
	@FramerFlex26.setter
	def FramerFlex26(self, new_state):
		self._setter_access_tracker["FramerFlex26"] = {}
		self._FramerFlex26 = FramerFlex(new_state)

	@property
	def FramerFlex27(self):
		self._getter_access_tracker["FramerFlex27"] = {}
		return self._FramerFlex27
	@FramerFlex27.setter
	def FramerFlex27(self, new_state):
		self._setter_access_tracker["FramerFlex27"] = {}
		self._FramerFlex27 = FramerFlex(new_state)

	@property
	def Flex63(self):
		self._getter_access_tracker["Flex63"] = {}
		return self._Flex63
	@Flex63.setter
	def Flex63(self, new_state):
		self._setter_access_tracker["Flex63"] = {}
		self._Flex63 = Flex(new_state)

	@property
	def Image25(self):
		self._getter_access_tracker["Image25"] = {}
		return self._Image25
	@Image25.setter
	def Image25(self, new_state):
		self._setter_access_tracker["Image25"] = {}
		self._Image25 = Image(new_state)

	@property
	def TextBox61(self):
		self._getter_access_tracker["TextBox61"] = {}
		return self._TextBox61
	@TextBox61.setter
	def TextBox61(self, new_state):
		self._setter_access_tracker["TextBox61"] = {}
		self._TextBox61 = TextBox(new_state)

	@property
	def TextBox62(self):
		self._getter_access_tracker["TextBox62"] = {}
		return self._TextBox62
	@TextBox62.setter
	def TextBox62(self, new_state):
		self._setter_access_tracker["TextBox62"] = {}
		self._TextBox62 = TextBox(new_state)

	@property
	def Image26(self):
		self._getter_access_tracker["Image26"] = {}
		return self._Image26
	@Image26.setter
	def Image26(self, new_state):
		self._setter_access_tracker["Image26"] = {}
		self._Image26 = Image(new_state)

	@property
	def ScaleFlex17(self):
		self._getter_access_tracker["ScaleFlex17"] = {}
		return self._ScaleFlex17
	@ScaleFlex17.setter
	def ScaleFlex17(self, new_state):
		self._setter_access_tracker["ScaleFlex17"] = {}
		self._ScaleFlex17 = ScaleFlex(new_state)

	@property
	def ScaleFlex18(self):
		self._getter_access_tracker["ScaleFlex18"] = {}
		return self._ScaleFlex18
	@ScaleFlex18.setter
	def ScaleFlex18(self, new_state):
		self._setter_access_tracker["ScaleFlex18"] = {}
		self._ScaleFlex18 = ScaleFlex(new_state)

	@property
	def Anchor76(self):
		self._getter_access_tracker["Anchor76"] = {}
		return self._Anchor76
	@Anchor76.setter
	def Anchor76(self, new_state):
		self._setter_access_tracker["Anchor76"] = {}
		self._Anchor76 = Anchor(new_state)

	@property
	def Anchor77(self):
		self._getter_access_tracker["Anchor77"] = {}
		return self._Anchor77
	@Anchor77.setter
	def Anchor77(self, new_state):
		self._setter_access_tracker["Anchor77"] = {}
		self._Anchor77 = Anchor(new_state)

	@property
	def FramerFlex28(self):
		self._getter_access_tracker["FramerFlex28"] = {}
		return self._FramerFlex28
	@FramerFlex28.setter
	def FramerFlex28(self, new_state):
		self._setter_access_tracker["FramerFlex28"] = {}
		self._FramerFlex28 = FramerFlex(new_state)

	@property
	def FramerFlex29(self):
		self._getter_access_tracker["FramerFlex29"] = {}
		return self._FramerFlex29
	@FramerFlex29.setter
	def FramerFlex29(self, new_state):
		self._setter_access_tracker["FramerFlex29"] = {}
		self._FramerFlex29 = FramerFlex(new_state)

	@property
	def Flex64(self):
		self._getter_access_tracker["Flex64"] = {}
		return self._Flex64
	@Flex64.setter
	def Flex64(self, new_state):
		self._setter_access_tracker["Flex64"] = {}
		self._Flex64 = Flex(new_state)

	@property
	def Image27(self):
		self._getter_access_tracker["Image27"] = {}
		return self._Image27
	@Image27.setter
	def Image27(self, new_state):
		self._setter_access_tracker["Image27"] = {}
		self._Image27 = Image(new_state)

	@property
	def TextBox63(self):
		self._getter_access_tracker["TextBox63"] = {}
		return self._TextBox63
	@TextBox63.setter
	def TextBox63(self, new_state):
		self._setter_access_tracker["TextBox63"] = {}
		self._TextBox63 = TextBox(new_state)

	@property
	def TextBox64(self):
		self._getter_access_tracker["TextBox64"] = {}
		return self._TextBox64
	@TextBox64.setter
	def TextBox64(self, new_state):
		self._setter_access_tracker["TextBox64"] = {}
		self._TextBox64 = TextBox(new_state)

	@property
	def Image28(self):
		self._getter_access_tracker["Image28"] = {}
		return self._Image28
	@Image28.setter
	def Image28(self, new_state):
		self._setter_access_tracker["Image28"] = {}
		self._Image28 = Image(new_state)

	@property
	def ScaleFlex19(self):
		self._getter_access_tracker["ScaleFlex19"] = {}
		return self._ScaleFlex19
	@ScaleFlex19.setter
	def ScaleFlex19(self, new_state):
		self._setter_access_tracker["ScaleFlex19"] = {}
		self._ScaleFlex19 = ScaleFlex(new_state)

	@property
	def ScaleFlex20(self):
		self._getter_access_tracker["ScaleFlex20"] = {}
		return self._ScaleFlex20
	@ScaleFlex20.setter
	def ScaleFlex20(self, new_state):
		self._setter_access_tracker["ScaleFlex20"] = {}
		self._ScaleFlex20 = ScaleFlex(new_state)

	@property
	def Anchor78(self):
		self._getter_access_tracker["Anchor78"] = {}
		return self._Anchor78
	@Anchor78.setter
	def Anchor78(self, new_state):
		self._setter_access_tracker["Anchor78"] = {}
		self._Anchor78 = Anchor(new_state)

	@property
	def Anchor79(self):
		self._getter_access_tracker["Anchor79"] = {}
		return self._Anchor79
	@Anchor79.setter
	def Anchor79(self, new_state):
		self._setter_access_tracker["Anchor79"] = {}
		self._Anchor79 = Anchor(new_state)

	@property
	def FramerFlex30(self):
		self._getter_access_tracker["FramerFlex30"] = {}
		return self._FramerFlex30
	@FramerFlex30.setter
	def FramerFlex30(self, new_state):
		self._setter_access_tracker["FramerFlex30"] = {}
		self._FramerFlex30 = FramerFlex(new_state)

	@property
	def FramerFlex31(self):
		self._getter_access_tracker["FramerFlex31"] = {}
		return self._FramerFlex31
	@FramerFlex31.setter
	def FramerFlex31(self, new_state):
		self._setter_access_tracker["FramerFlex31"] = {}
		self._FramerFlex31 = FramerFlex(new_state)

	@property
	def Flex65(self):
		self._getter_access_tracker["Flex65"] = {}
		return self._Flex65
	@Flex65.setter
	def Flex65(self, new_state):
		self._setter_access_tracker["Flex65"] = {}
		self._Flex65 = Flex(new_state)

	@property
	def Image29(self):
		self._getter_access_tracker["Image29"] = {}
		return self._Image29
	@Image29.setter
	def Image29(self, new_state):
		self._setter_access_tracker["Image29"] = {}
		self._Image29 = Image(new_state)

	@property
	def TextBox65(self):
		self._getter_access_tracker["TextBox65"] = {}
		return self._TextBox65
	@TextBox65.setter
	def TextBox65(self, new_state):
		self._setter_access_tracker["TextBox65"] = {}
		self._TextBox65 = TextBox(new_state)

	@property
	def TextBox66(self):
		self._getter_access_tracker["TextBox66"] = {}
		return self._TextBox66
	@TextBox66.setter
	def TextBox66(self, new_state):
		self._setter_access_tracker["TextBox66"] = {}
		self._TextBox66 = TextBox(new_state)

	@property
	def Image30(self):
		self._getter_access_tracker["Image30"] = {}
		return self._Image30
	@Image30.setter
	def Image30(self, new_state):
		self._setter_access_tracker["Image30"] = {}
		self._Image30 = Image(new_state)

	@property
	def ScaleFlex21(self):
		self._getter_access_tracker["ScaleFlex21"] = {}
		return self._ScaleFlex21
	@ScaleFlex21.setter
	def ScaleFlex21(self, new_state):
		self._setter_access_tracker["ScaleFlex21"] = {}
		self._ScaleFlex21 = ScaleFlex(new_state)

	@property
	def ScaleFlex22(self):
		self._getter_access_tracker["ScaleFlex22"] = {}
		return self._ScaleFlex22
	@ScaleFlex22.setter
	def ScaleFlex22(self, new_state):
		self._setter_access_tracker["ScaleFlex22"] = {}
		self._ScaleFlex22 = ScaleFlex(new_state)

	@property
	def Anchor80(self):
		self._getter_access_tracker["Anchor80"] = {}
		return self._Anchor80
	@Anchor80.setter
	def Anchor80(self, new_state):
		self._setter_access_tracker["Anchor80"] = {}
		self._Anchor80 = Anchor(new_state)

	@property
	def Anchor81(self):
		self._getter_access_tracker["Anchor81"] = {}
		return self._Anchor81
	@Anchor81.setter
	def Anchor81(self, new_state):
		self._setter_access_tracker["Anchor81"] = {}
		self._Anchor81 = Anchor(new_state)

	@property
	def FramerFlex32(self):
		self._getter_access_tracker["FramerFlex32"] = {}
		return self._FramerFlex32
	@FramerFlex32.setter
	def FramerFlex32(self, new_state):
		self._setter_access_tracker["FramerFlex32"] = {}
		self._FramerFlex32 = FramerFlex(new_state)

	@property
	def FramerFlex33(self):
		self._getter_access_tracker["FramerFlex33"] = {}
		return self._FramerFlex33
	@FramerFlex33.setter
	def FramerFlex33(self, new_state):
		self._setter_access_tracker["FramerFlex33"] = {}
		self._FramerFlex33 = FramerFlex(new_state)

	@property
	def Flex66(self):
		self._getter_access_tracker["Flex66"] = {}
		return self._Flex66
	@Flex66.setter
	def Flex66(self, new_state):
		self._setter_access_tracker["Flex66"] = {}
		self._Flex66 = Flex(new_state)

	@property
	def Image31(self):
		self._getter_access_tracker["Image31"] = {}
		return self._Image31
	@Image31.setter
	def Image31(self, new_state):
		self._setter_access_tracker["Image31"] = {}
		self._Image31 = Image(new_state)

	@property
	def TextBox67(self):
		self._getter_access_tracker["TextBox67"] = {}
		return self._TextBox67
	@TextBox67.setter
	def TextBox67(self, new_state):
		self._setter_access_tracker["TextBox67"] = {}
		self._TextBox67 = TextBox(new_state)

	@property
	def TextBox68(self):
		self._getter_access_tracker["TextBox68"] = {}
		return self._TextBox68
	@TextBox68.setter
	def TextBox68(self, new_state):
		self._setter_access_tracker["TextBox68"] = {}
		self._TextBox68 = TextBox(new_state)

	@property
	def Image32(self):
		self._getter_access_tracker["Image32"] = {}
		return self._Image32
	@Image32.setter
	def Image32(self, new_state):
		self._setter_access_tracker["Image32"] = {}
		self._Image32 = Image(new_state)

	@property
	def ScaleFlex23(self):
		self._getter_access_tracker["ScaleFlex23"] = {}
		return self._ScaleFlex23
	@ScaleFlex23.setter
	def ScaleFlex23(self, new_state):
		self._setter_access_tracker["ScaleFlex23"] = {}
		self._ScaleFlex23 = ScaleFlex(new_state)

	@property
	def ScaleFlex24(self):
		self._getter_access_tracker["ScaleFlex24"] = {}
		return self._ScaleFlex24
	@ScaleFlex24.setter
	def ScaleFlex24(self, new_state):
		self._setter_access_tracker["ScaleFlex24"] = {}
		self._ScaleFlex24 = ScaleFlex(new_state)

	@property
	def Anchor82(self):
		self._getter_access_tracker["Anchor82"] = {}
		return self._Anchor82
	@Anchor82.setter
	def Anchor82(self, new_state):
		self._setter_access_tracker["Anchor82"] = {}
		self._Anchor82 = Anchor(new_state)

	@property
	def Anchor83(self):
		self._getter_access_tracker["Anchor83"] = {}
		return self._Anchor83
	@Anchor83.setter
	def Anchor83(self, new_state):
		self._setter_access_tracker["Anchor83"] = {}
		self._Anchor83 = Anchor(new_state)

	@property
	def FramerFlex34(self):
		self._getter_access_tracker["FramerFlex34"] = {}
		return self._FramerFlex34
	@FramerFlex34.setter
	def FramerFlex34(self, new_state):
		self._setter_access_tracker["FramerFlex34"] = {}
		self._FramerFlex34 = FramerFlex(new_state)

	@property
	def FramerFlex35(self):
		self._getter_access_tracker["FramerFlex35"] = {}
		return self._FramerFlex35
	@FramerFlex35.setter
	def FramerFlex35(self, new_state):
		self._setter_access_tracker["FramerFlex35"] = {}
		self._FramerFlex35 = FramerFlex(new_state)

	@property
	def Flex67(self):
		self._getter_access_tracker["Flex67"] = {}
		return self._Flex67
	@Flex67.setter
	def Flex67(self, new_state):
		self._setter_access_tracker["Flex67"] = {}
		self._Flex67 = Flex(new_state)

	@property
	def Image33(self):
		self._getter_access_tracker["Image33"] = {}
		return self._Image33
	@Image33.setter
	def Image33(self, new_state):
		self._setter_access_tracker["Image33"] = {}
		self._Image33 = Image(new_state)

	@property
	def TextBox69(self):
		self._getter_access_tracker["TextBox69"] = {}
		return self._TextBox69
	@TextBox69.setter
	def TextBox69(self, new_state):
		self._setter_access_tracker["TextBox69"] = {}
		self._TextBox69 = TextBox(new_state)

	@property
	def TextBox70(self):
		self._getter_access_tracker["TextBox70"] = {}
		return self._TextBox70
	@TextBox70.setter
	def TextBox70(self, new_state):
		self._setter_access_tracker["TextBox70"] = {}
		self._TextBox70 = TextBox(new_state)

	@property
	def Image34(self):
		self._getter_access_tracker["Image34"] = {}
		return self._Image34
	@Image34.setter
	def Image34(self, new_state):
		self._setter_access_tracker["Image34"] = {}
		self._Image34 = Image(new_state)

	@property
	def ScaleFlex25(self):
		self._getter_access_tracker["ScaleFlex25"] = {}
		return self._ScaleFlex25
	@ScaleFlex25.setter
	def ScaleFlex25(self, new_state):
		self._setter_access_tracker["ScaleFlex25"] = {}
		self._ScaleFlex25 = ScaleFlex(new_state)

	@property
	def ScaleFlex26(self):
		self._getter_access_tracker["ScaleFlex26"] = {}
		return self._ScaleFlex26
	@ScaleFlex26.setter
	def ScaleFlex26(self, new_state):
		self._setter_access_tracker["ScaleFlex26"] = {}
		self._ScaleFlex26 = ScaleFlex(new_state)

	@property
	def Anchor84(self):
		self._getter_access_tracker["Anchor84"] = {}
		return self._Anchor84
	@Anchor84.setter
	def Anchor84(self, new_state):
		self._setter_access_tracker["Anchor84"] = {}
		self._Anchor84 = Anchor(new_state)

	@property
	def Anchor85(self):
		self._getter_access_tracker["Anchor85"] = {}
		return self._Anchor85
	@Anchor85.setter
	def Anchor85(self, new_state):
		self._setter_access_tracker["Anchor85"] = {}
		self._Anchor85 = Anchor(new_state)

	@property
	def FramerFlex36(self):
		self._getter_access_tracker["FramerFlex36"] = {}
		return self._FramerFlex36
	@FramerFlex36.setter
	def FramerFlex36(self, new_state):
		self._setter_access_tracker["FramerFlex36"] = {}
		self._FramerFlex36 = FramerFlex(new_state)

	@property
	def FramerFlex37(self):
		self._getter_access_tracker["FramerFlex37"] = {}
		return self._FramerFlex37
	@FramerFlex37.setter
	def FramerFlex37(self, new_state):
		self._setter_access_tracker["FramerFlex37"] = {}
		self._FramerFlex37 = FramerFlex(new_state)

	@property
	def Flex68(self):
		self._getter_access_tracker["Flex68"] = {}
		return self._Flex68
	@Flex68.setter
	def Flex68(self, new_state):
		self._setter_access_tracker["Flex68"] = {}
		self._Flex68 = Flex(new_state)

	@property
	def TextBox71(self):
		self._getter_access_tracker["TextBox71"] = {}
		return self._TextBox71
	@TextBox71.setter
	def TextBox71(self, new_state):
		self._setter_access_tracker["TextBox71"] = {}
		self._TextBox71 = TextBox(new_state)

	@property
	def TextBox72(self):
		self._getter_access_tracker["TextBox72"] = {}
		return self._TextBox72
	@TextBox72.setter
	def TextBox72(self, new_state):
		self._setter_access_tracker["TextBox72"] = {}
		self._TextBox72 = TextBox(new_state)

	@property
	def ButtonFlex13(self):
		self._getter_access_tracker["ButtonFlex13"] = {}
		return self._ButtonFlex13
	@ButtonFlex13.setter
	def ButtonFlex13(self, new_state):
		self._setter_access_tracker["ButtonFlex13"] = {}
		self._ButtonFlex13 = ButtonFlex(new_state)

	@property
	def Anchor86(self):
		self._getter_access_tracker["Anchor86"] = {}
		return self._Anchor86
	@Anchor86.setter
	def Anchor86(self, new_state):
		self._setter_access_tracker["Anchor86"] = {}
		self._Anchor86 = Anchor(new_state)

	@property
	def Flex69(self):
		self._getter_access_tracker["Flex69"] = {}
		return self._Flex69
	@Flex69.setter
	def Flex69(self, new_state):
		self._setter_access_tracker["Flex69"] = {}
		self._Flex69 = Flex(new_state)

	@property
	def Flex70(self):
		self._getter_access_tracker["Flex70"] = {}
		return self._Flex70
	@Flex70.setter
	def Flex70(self, new_state):
		self._setter_access_tracker["Flex70"] = {}
		self._Flex70 = Flex(new_state)

	@property
	def Flex71(self):
		self._getter_access_tracker["Flex71"] = {}
		return self._Flex71
	@Flex71.setter
	def Flex71(self, new_state):
		self._setter_access_tracker["Flex71"] = {}
		self._Flex71 = Flex(new_state)

	@property
	def Flex72(self):
		self._getter_access_tracker["Flex72"] = {}
		return self._Flex72
	@Flex72.setter
	def Flex72(self, new_state):
		self._setter_access_tracker["Flex72"] = {}
		self._Flex72 = Flex(new_state)

	@property
	def TextBox73(self):
		self._getter_access_tracker["TextBox73"] = {}
		return self._TextBox73
	@TextBox73.setter
	def TextBox73(self, new_state):
		self._setter_access_tracker["TextBox73"] = {}
		self._TextBox73 = TextBox(new_state)

	@property
	def Div13(self):
		self._getter_access_tracker["Div13"] = {}
		return self._Div13
	@Div13.setter
	def Div13(self, new_state):
		self._setter_access_tracker["Div13"] = {}
		self._Div13 = Div(new_state)

	@property
	def FramerFlex38(self):
		self._getter_access_tracker["FramerFlex38"] = {}
		return self._FramerFlex38
	@FramerFlex38.setter
	def FramerFlex38(self, new_state):
		self._setter_access_tracker["FramerFlex38"] = {}
		self._FramerFlex38 = FramerFlex(new_state)

	@property
	def Flex73(self):
		self._getter_access_tracker["Flex73"] = {}
		return self._Flex73
	@Flex73.setter
	def Flex73(self, new_state):
		self._setter_access_tracker["Flex73"] = {}
		self._Flex73 = Flex(new_state)

	@property
	def Image35(self):
		self._getter_access_tracker["Image35"] = {}
		return self._Image35
	@Image35.setter
	def Image35(self, new_state):
		self._setter_access_tracker["Image35"] = {}
		self._Image35 = Image(new_state)

	@property
	def TextBox74(self):
		self._getter_access_tracker["TextBox74"] = {}
		return self._TextBox74
	@TextBox74.setter
	def TextBox74(self, new_state):
		self._setter_access_tracker["TextBox74"] = {}
		self._TextBox74 = TextBox(new_state)

	@property
	def TextBox75(self):
		self._getter_access_tracker["TextBox75"] = {}
		return self._TextBox75
	@TextBox75.setter
	def TextBox75(self, new_state):
		self._setter_access_tracker["TextBox75"] = {}
		self._TextBox75 = TextBox(new_state)

	@property
	def Image36(self):
		self._getter_access_tracker["Image36"] = {}
		return self._Image36
	@Image36.setter
	def Image36(self, new_state):
		self._setter_access_tracker["Image36"] = {}
		self._Image36 = Image(new_state)

	@property
	def ScaleFlex27(self):
		self._getter_access_tracker["ScaleFlex27"] = {}
		return self._ScaleFlex27
	@ScaleFlex27.setter
	def ScaleFlex27(self, new_state):
		self._setter_access_tracker["ScaleFlex27"] = {}
		self._ScaleFlex27 = ScaleFlex(new_state)

	@property
	def ScaleFlex28(self):
		self._getter_access_tracker["ScaleFlex28"] = {}
		return self._ScaleFlex28
	@ScaleFlex28.setter
	def ScaleFlex28(self, new_state):
		self._setter_access_tracker["ScaleFlex28"] = {}
		self._ScaleFlex28 = ScaleFlex(new_state)

	@property
	def Anchor87(self):
		self._getter_access_tracker["Anchor87"] = {}
		return self._Anchor87
	@Anchor87.setter
	def Anchor87(self, new_state):
		self._setter_access_tracker["Anchor87"] = {}
		self._Anchor87 = Anchor(new_state)

	@property
	def Anchor88(self):
		self._getter_access_tracker["Anchor88"] = {}
		return self._Anchor88
	@Anchor88.setter
	def Anchor88(self, new_state):
		self._setter_access_tracker["Anchor88"] = {}
		self._Anchor88 = Anchor(new_state)

	@property
	def FramerFlex39(self):
		self._getter_access_tracker["FramerFlex39"] = {}
		return self._FramerFlex39
	@FramerFlex39.setter
	def FramerFlex39(self, new_state):
		self._setter_access_tracker["FramerFlex39"] = {}
		self._FramerFlex39 = FramerFlex(new_state)

	@property
	def FramerFlex40(self):
		self._getter_access_tracker["FramerFlex40"] = {}
		return self._FramerFlex40
	@FramerFlex40.setter
	def FramerFlex40(self, new_state):
		self._setter_access_tracker["FramerFlex40"] = {}
		self._FramerFlex40 = FramerFlex(new_state)

	@property
	def Flex74(self):
		self._getter_access_tracker["Flex74"] = {}
		return self._Flex74
	@Flex74.setter
	def Flex74(self, new_state):
		self._setter_access_tracker["Flex74"] = {}
		self._Flex74 = Flex(new_state)

	@property
	def Image37(self):
		self._getter_access_tracker["Image37"] = {}
		return self._Image37
	@Image37.setter
	def Image37(self, new_state):
		self._setter_access_tracker["Image37"] = {}
		self._Image37 = Image(new_state)

	@property
	def TextBox76(self):
		self._getter_access_tracker["TextBox76"] = {}
		return self._TextBox76
	@TextBox76.setter
	def TextBox76(self, new_state):
		self._setter_access_tracker["TextBox76"] = {}
		self._TextBox76 = TextBox(new_state)

	@property
	def TextBox77(self):
		self._getter_access_tracker["TextBox77"] = {}
		return self._TextBox77
	@TextBox77.setter
	def TextBox77(self, new_state):
		self._setter_access_tracker["TextBox77"] = {}
		self._TextBox77 = TextBox(new_state)

	@property
	def Image38(self):
		self._getter_access_tracker["Image38"] = {}
		return self._Image38
	@Image38.setter
	def Image38(self, new_state):
		self._setter_access_tracker["Image38"] = {}
		self._Image38 = Image(new_state)

	@property
	def ScaleFlex29(self):
		self._getter_access_tracker["ScaleFlex29"] = {}
		return self._ScaleFlex29
	@ScaleFlex29.setter
	def ScaleFlex29(self, new_state):
		self._setter_access_tracker["ScaleFlex29"] = {}
		self._ScaleFlex29 = ScaleFlex(new_state)

	@property
	def ScaleFlex30(self):
		self._getter_access_tracker["ScaleFlex30"] = {}
		return self._ScaleFlex30
	@ScaleFlex30.setter
	def ScaleFlex30(self, new_state):
		self._setter_access_tracker["ScaleFlex30"] = {}
		self._ScaleFlex30 = ScaleFlex(new_state)

	@property
	def Anchor89(self):
		self._getter_access_tracker["Anchor89"] = {}
		return self._Anchor89
	@Anchor89.setter
	def Anchor89(self, new_state):
		self._setter_access_tracker["Anchor89"] = {}
		self._Anchor89 = Anchor(new_state)

	@property
	def Anchor90(self):
		self._getter_access_tracker["Anchor90"] = {}
		return self._Anchor90
	@Anchor90.setter
	def Anchor90(self, new_state):
		self._setter_access_tracker["Anchor90"] = {}
		self._Anchor90 = Anchor(new_state)

	@property
	def FramerFlex41(self):
		self._getter_access_tracker["FramerFlex41"] = {}
		return self._FramerFlex41
	@FramerFlex41.setter
	def FramerFlex41(self, new_state):
		self._setter_access_tracker["FramerFlex41"] = {}
		self._FramerFlex41 = FramerFlex(new_state)

	@property
	def FramerFlex42(self):
		self._getter_access_tracker["FramerFlex42"] = {}
		return self._FramerFlex42
	@FramerFlex42.setter
	def FramerFlex42(self, new_state):
		self._setter_access_tracker["FramerFlex42"] = {}
		self._FramerFlex42 = FramerFlex(new_state)

	@property
	def Flex75(self):
		self._getter_access_tracker["Flex75"] = {}
		return self._Flex75
	@Flex75.setter
	def Flex75(self, new_state):
		self._setter_access_tracker["Flex75"] = {}
		self._Flex75 = Flex(new_state)

	@property
	def Image39(self):
		self._getter_access_tracker["Image39"] = {}
		return self._Image39
	@Image39.setter
	def Image39(self, new_state):
		self._setter_access_tracker["Image39"] = {}
		self._Image39 = Image(new_state)

	@property
	def TextBox78(self):
		self._getter_access_tracker["TextBox78"] = {}
		return self._TextBox78
	@TextBox78.setter
	def TextBox78(self, new_state):
		self._setter_access_tracker["TextBox78"] = {}
		self._TextBox78 = TextBox(new_state)

	@property
	def TextBox79(self):
		self._getter_access_tracker["TextBox79"] = {}
		return self._TextBox79
	@TextBox79.setter
	def TextBox79(self, new_state):
		self._setter_access_tracker["TextBox79"] = {}
		self._TextBox79 = TextBox(new_state)

	@property
	def Image40(self):
		self._getter_access_tracker["Image40"] = {}
		return self._Image40
	@Image40.setter
	def Image40(self, new_state):
		self._setter_access_tracker["Image40"] = {}
		self._Image40 = Image(new_state)

	@property
	def ScaleFlex31(self):
		self._getter_access_tracker["ScaleFlex31"] = {}
		return self._ScaleFlex31
	@ScaleFlex31.setter
	def ScaleFlex31(self, new_state):
		self._setter_access_tracker["ScaleFlex31"] = {}
		self._ScaleFlex31 = ScaleFlex(new_state)

	@property
	def ScaleFlex32(self):
		self._getter_access_tracker["ScaleFlex32"] = {}
		return self._ScaleFlex32
	@ScaleFlex32.setter
	def ScaleFlex32(self, new_state):
		self._setter_access_tracker["ScaleFlex32"] = {}
		self._ScaleFlex32 = ScaleFlex(new_state)

	@property
	def Anchor91(self):
		self._getter_access_tracker["Anchor91"] = {}
		return self._Anchor91
	@Anchor91.setter
	def Anchor91(self, new_state):
		self._setter_access_tracker["Anchor91"] = {}
		self._Anchor91 = Anchor(new_state)

	@property
	def Anchor92(self):
		self._getter_access_tracker["Anchor92"] = {}
		return self._Anchor92
	@Anchor92.setter
	def Anchor92(self, new_state):
		self._setter_access_tracker["Anchor92"] = {}
		self._Anchor92 = Anchor(new_state)

	@property
	def FramerFlex43(self):
		self._getter_access_tracker["FramerFlex43"] = {}
		return self._FramerFlex43
	@FramerFlex43.setter
	def FramerFlex43(self, new_state):
		self._setter_access_tracker["FramerFlex43"] = {}
		self._FramerFlex43 = FramerFlex(new_state)

	@property
	def FramerFlex44(self):
		self._getter_access_tracker["FramerFlex44"] = {}
		return self._FramerFlex44
	@FramerFlex44.setter
	def FramerFlex44(self, new_state):
		self._setter_access_tracker["FramerFlex44"] = {}
		self._FramerFlex44 = FramerFlex(new_state)

	@property
	def Flex76(self):
		self._getter_access_tracker["Flex76"] = {}
		return self._Flex76
	@Flex76.setter
	def Flex76(self, new_state):
		self._setter_access_tracker["Flex76"] = {}
		self._Flex76 = Flex(new_state)

	@property
	def Image41(self):
		self._getter_access_tracker["Image41"] = {}
		return self._Image41
	@Image41.setter
	def Image41(self, new_state):
		self._setter_access_tracker["Image41"] = {}
		self._Image41 = Image(new_state)

	@property
	def TextBox80(self):
		self._getter_access_tracker["TextBox80"] = {}
		return self._TextBox80
	@TextBox80.setter
	def TextBox80(self, new_state):
		self._setter_access_tracker["TextBox80"] = {}
		self._TextBox80 = TextBox(new_state)

	@property
	def TextBox81(self):
		self._getter_access_tracker["TextBox81"] = {}
		return self._TextBox81
	@TextBox81.setter
	def TextBox81(self, new_state):
		self._setter_access_tracker["TextBox81"] = {}
		self._TextBox81 = TextBox(new_state)

	@property
	def Image42(self):
		self._getter_access_tracker["Image42"] = {}
		return self._Image42
	@Image42.setter
	def Image42(self, new_state):
		self._setter_access_tracker["Image42"] = {}
		self._Image42 = Image(new_state)

	@property
	def ScaleFlex33(self):
		self._getter_access_tracker["ScaleFlex33"] = {}
		return self._ScaleFlex33
	@ScaleFlex33.setter
	def ScaleFlex33(self, new_state):
		self._setter_access_tracker["ScaleFlex33"] = {}
		self._ScaleFlex33 = ScaleFlex(new_state)

	@property
	def ScaleFlex34(self):
		self._getter_access_tracker["ScaleFlex34"] = {}
		return self._ScaleFlex34
	@ScaleFlex34.setter
	def ScaleFlex34(self, new_state):
		self._setter_access_tracker["ScaleFlex34"] = {}
		self._ScaleFlex34 = ScaleFlex(new_state)

	@property
	def Anchor93(self):
		self._getter_access_tracker["Anchor93"] = {}
		return self._Anchor93
	@Anchor93.setter
	def Anchor93(self, new_state):
		self._setter_access_tracker["Anchor93"] = {}
		self._Anchor93 = Anchor(new_state)

	@property
	def Anchor94(self):
		self._getter_access_tracker["Anchor94"] = {}
		return self._Anchor94
	@Anchor94.setter
	def Anchor94(self, new_state):
		self._setter_access_tracker["Anchor94"] = {}
		self._Anchor94 = Anchor(new_state)

	@property
	def FramerFlex45(self):
		self._getter_access_tracker["FramerFlex45"] = {}
		return self._FramerFlex45
	@FramerFlex45.setter
	def FramerFlex45(self, new_state):
		self._setter_access_tracker["FramerFlex45"] = {}
		self._FramerFlex45 = FramerFlex(new_state)

	@property
	def FramerFlex46(self):
		self._getter_access_tracker["FramerFlex46"] = {}
		return self._FramerFlex46
	@FramerFlex46.setter
	def FramerFlex46(self, new_state):
		self._setter_access_tracker["FramerFlex46"] = {}
		self._FramerFlex46 = FramerFlex(new_state)

	@property
	def Flex77(self):
		self._getter_access_tracker["Flex77"] = {}
		return self._Flex77
	@Flex77.setter
	def Flex77(self, new_state):
		self._setter_access_tracker["Flex77"] = {}
		self._Flex77 = Flex(new_state)

	@property
	def TextBox84(self):
		self._getter_access_tracker["TextBox84"] = {}
		return self._TextBox84
	@TextBox84.setter
	def TextBox84(self, new_state):
		self._setter_access_tracker["TextBox84"] = {}
		self._TextBox84 = TextBox(new_state)

	@property
	def TextBox85(self):
		self._getter_access_tracker["TextBox85"] = {}
		return self._TextBox85
	@TextBox85.setter
	def TextBox85(self, new_state):
		self._setter_access_tracker["TextBox85"] = {}
		self._TextBox85 = TextBox(new_state)

	@property
	def ButtonFlex14(self):
		self._getter_access_tracker["ButtonFlex14"] = {}
		return self._ButtonFlex14
	@ButtonFlex14.setter
	def ButtonFlex14(self, new_state):
		self._setter_access_tracker["ButtonFlex14"] = {}
		self._ButtonFlex14 = ButtonFlex(new_state)

	@property
	def Anchor97(self):
		self._getter_access_tracker["Anchor97"] = {}
		return self._Anchor97
	@Anchor97.setter
	def Anchor97(self, new_state):
		self._setter_access_tracker["Anchor97"] = {}
		self._Anchor97 = Anchor(new_state)

	@property
	def Flex79(self):
		self._getter_access_tracker["Flex79"] = {}
		return self._Flex79
	@Flex79.setter
	def Flex79(self, new_state):
		self._setter_access_tracker["Flex79"] = {}
		self._Flex79 = Flex(new_state)

	@property
	def Flex80(self):
		self._getter_access_tracker["Flex80"] = {}
		return self._Flex80
	@Flex80.setter
	def Flex80(self, new_state):
		self._setter_access_tracker["Flex80"] = {}
		self._Flex80 = Flex(new_state)

	@property
	def FramerFlex49(self):
		self._getter_access_tracker["FramerFlex49"] = {}
		return self._FramerFlex49
	@FramerFlex49.setter
	def FramerFlex49(self, new_state):
		self._setter_access_tracker["FramerFlex49"] = {}
		self._FramerFlex49 = FramerFlex(new_state)

	@property
	def Flex81(self):
		self._getter_access_tracker["Flex81"] = {}
		return self._Flex81
	@Flex81.setter
	def Flex81(self, new_state):
		self._setter_access_tracker["Flex81"] = {}
		self._Flex81 = Flex(new_state)

	@property
	def Flex82(self):
		self._getter_access_tracker["Flex82"] = {}
		return self._Flex82
	@Flex82.setter
	def Flex82(self, new_state):
		self._setter_access_tracker["Flex82"] = {}
		self._Flex82 = Flex(new_state)

	@property
	def TextBox86(self):
		self._getter_access_tracker["TextBox86"] = {}
		return self._TextBox86
	@TextBox86.setter
	def TextBox86(self, new_state):
		self._setter_access_tracker["TextBox86"] = {}
		self._TextBox86 = TextBox(new_state)

	@property
	def TextBox87(self):
		self._getter_access_tracker["TextBox87"] = {}
		return self._TextBox87
	@TextBox87.setter
	def TextBox87(self, new_state):
		self._setter_access_tracker["TextBox87"] = {}
		self._TextBox87 = TextBox(new_state)

	@property
	def TextBox88(self):
		self._getter_access_tracker["TextBox88"] = {}
		return self._TextBox88
	@TextBox88.setter
	def TextBox88(self, new_state):
		self._setter_access_tracker["TextBox88"] = {}
		self._TextBox88 = TextBox(new_state)

	@property
	def ButtonFlex15(self):
		self._getter_access_tracker["ButtonFlex15"] = {}
		return self._ButtonFlex15
	@ButtonFlex15.setter
	def ButtonFlex15(self, new_state):
		self._setter_access_tracker["ButtonFlex15"] = {}
		self._ButtonFlex15 = ButtonFlex(new_state)

	@property
	def Anchor98(self):
		self._getter_access_tracker["Anchor98"] = {}
		return self._Anchor98
	@Anchor98.setter
	def Anchor98(self, new_state):
		self._setter_access_tracker["Anchor98"] = {}
		self._Anchor98 = Anchor(new_state)
  
	def _to_json_fields(self):
		return {
			"TextBox1": self._TextBox1,
			"TextBox2": self._TextBox2,
			"TextBox3": self._TextBox3,
			"TextBox4": self._TextBox4,
			"ButtonFlex1": self._ButtonFlex1,
			"ButtonFlex2": self._ButtonFlex2,
			"Anchor1": self._Anchor1,
			"Anchor2": self._Anchor2,
			"FramerText1": self._FramerText1,
			"FramerText2": self._FramerText2,
			"FramerText3": self._FramerText3,
			"TextBox5": self._TextBox5,
			"TextBox6": self._TextBox6,
			"TextBox7": self._TextBox7,
			"TextBox8": self._TextBox8,
			"Flex1": self._Flex1,
			"Flex2": self._Flex2,
			"Anchor3": self._Anchor3,
			"Anchor4": self._Anchor4,
			"Anchor5": self._Anchor5,
			"Flex3": self._Flex3,
			"FramerText4": self._FramerText4,
			"FramerText5": self._FramerText5,
			"FramerText6": self._FramerText6,
			"FramerText7": self._FramerText7,
			"Image1": self._Image1,
			"ButtonFlex3": self._ButtonFlex3,
			"ButtonFlex4": self._ButtonFlex4,
			"Flex4": self._Flex4,
			"Pages1": self._Pages1,
			"Anchor6": self._Anchor6,
			"Anchor7": self._Anchor7,
			"Anchor8": self._Anchor8,
			"Anchor9": self._Anchor9,
			"ScaleFlex1": self._ScaleFlex1,
			"Anchor10": self._Anchor10,
			"Anchor11": self._Anchor11,
			"DropdownMenu1": self._DropdownMenu1,
			"Flex5": self._Flex5,
			"Anchor12": self._Anchor12,
			"Flex6": self._Flex6,
			"Flex7": self._Flex7,
			"Flex8": self._Flex8,
			"Flex9": self._Flex9,
			"Flex10": self._Flex10,
			"Flex11": self._Flex11,
			"navbar1": self._navbar1,
			"Flex13": self._Flex13,
			"TextBox9": self._TextBox9,
			"TextBox10": self._TextBox10,
			"TextBox11": self._TextBox11,
			"TextBox12": self._TextBox12,
			"ButtonFlex5": self._ButtonFlex5,
			"ButtonFlex6": self._ButtonFlex6,
			"Anchor13": self._Anchor13,
			"Anchor14": self._Anchor14,
			"buttons1": self._buttons1,
			"TextBox13": self._TextBox13,
			"Image2": self._Image2,
			"TextBox14": self._TextBox14,
			"Image3": self._Image3,
			"TextBox15": self._TextBox15,
			"Image4": self._Image4,
			"TextBox16": self._TextBox16,
			"Image5": self._Image5,
			"TextBox17": self._TextBox17,
			"Image6": self._Image6,
			"TextBox18": self._TextBox18,
			"Image7": self._Image7,
			"FramerText8": self._FramerText8,
			"FramerText9": self._FramerText9,
			"FramerText10": self._FramerText10,
			"FramerText11": self._FramerText11,
			"FramerText12": self._FramerText12,
			"FramerText13": self._FramerText13,
			"FramerText14": self._FramerText14,
			"FramerText15": self._FramerText15,
			"FramerText16": self._FramerText16,
			"FramerText17": self._FramerText17,
			"FramerText18": self._FramerText18,
			"FramerText19": self._FramerText19,
			"FramerText20": self._FramerText20,
			"FramerText21": self._FramerText21,
			"FramerText22": self._FramerText22,
			"FramerText23": self._FramerText23,
			"FramerText24": self._FramerText24,
			"FramerText25": self._FramerText25,
			"FramerText26": self._FramerText26,
			"FramerText27": self._FramerText27,
			"FramerText28": self._FramerText28,
			"FramerText29": self._FramerText29,
			"FramerText30": self._FramerText30,
			"ButtonFlex7": self._ButtonFlex7,
			"ButtonFlex8": self._ButtonFlex8,
			"ButtonFlex9": self._ButtonFlex9,
			"ButtonFlex10": self._ButtonFlex10,
			"ButtonFlex11": self._ButtonFlex11,
			"ButtonFlex12": self._ButtonFlex12,
			"LineText1": self._LineText1,
			"FramerText31": self._FramerText31,
			"FramerText32": self._FramerText32,
			"FramerText33": self._FramerText33,
			"FramerText34": self._FramerText34,
			"FramerText35": self._FramerText35,
			"FramerText36": self._FramerText36,
			"FramerText37": self._FramerText37,
			"FramerText38": self._FramerText38,
			"FramerText39": self._FramerText39,
			"FramerText40": self._FramerText40,
			"FramerText41": self._FramerText41,
			"FramerText42": self._FramerText42,
			"Anchor15": self._Anchor15,
			"Anchor16": self._Anchor16,
			"Anchor17": self._Anchor17,
			"Anchor18": self._Anchor18,
			"Anchor19": self._Anchor19,
			"Anchor20": self._Anchor20,
			"Anchor21": self._Anchor21,
			"Anchor22": self._Anchor22,
			"Anchor23": self._Anchor23,
			"Anchor24": self._Anchor24,
			"Anchor25": self._Anchor25,
			"Anchor26": self._Anchor26,
			"Anchor27": self._Anchor27,
			"Anchor28": self._Anchor28,
			"Anchor29": self._Anchor29,
			"Anchor30": self._Anchor30,
			"Anchor31": self._Anchor31,
			"Anchor32": self._Anchor32,
			"Anchor33": self._Anchor33,
			"Anchor34": self._Anchor34,
			"Anchor35": self._Anchor35,
			"Anchor36": self._Anchor36,
			"Anchor37": self._Anchor37,
			"Anchor38": self._Anchor38,
			"Anchor39": self._Anchor39,
			"Anchor40": self._Anchor40,
			"Anchor41": self._Anchor41,
			"Anchor42": self._Anchor42,
			"Anchor43": self._Anchor43,
			"Anchor44": self._Anchor44,
			"Anchor45": self._Anchor45,
			"Anchor46": self._Anchor46,
			"Anchor47": self._Anchor47,
			"Anchor48": self._Anchor48,
			"Anchor49": self._Anchor49,
			"Anchor50": self._Anchor50,
			"Anchor51": self._Anchor51,
			"Anchor52": self._Anchor52,
			"Anchor53": self._Anchor53,
			"Anchor54": self._Anchor54,
			"Anchor55": self._Anchor55,
			"Anchor56": self._Anchor56,
			"Flex16": self._Flex16,
			"Flex17": self._Flex17,
			"Image8": self._Image8,
			"FramerText43": self._FramerText43,
			"FramerText44": self._FramerText44,
			"Flex18": self._Flex18,
			"TextBox19": self._TextBox19,
			"TextBox20": self._TextBox20,
			"Flex19": self._Flex19,
			"TextBox21": self._TextBox21,
			"Flex20": self._Flex20,
			"Flex21": self._Flex21,
			"TextBox22": self._TextBox22,
			"LineText2": self._LineText2,
			"LineText3": self._LineText3,
			"ScaleFlex2": self._ScaleFlex2,
			"Anchor57": self._Anchor57,
			"TextBox23": self._TextBox23,
			"Anchor58": self._Anchor58,
			"TextBox24": self._TextBox24,
			"Flex22": self._Flex22,
			"Flex23": self._Flex23,
			"Flex24": self._Flex24,
			"Flex25": self._Flex25,
			"Anchor59": self._Anchor59,
			"Anchor60": self._Anchor60,
			"Anchor61": self._Anchor61,
			"TextBox25": self._TextBox25,
			"Flex26": self._Flex26,
			"Div1": self._Div1,
			"Flex27": self._Flex27,
			"Flex28": self._Flex28,
			"Flex29": self._Flex29,
			"Flex30": self._Flex30,
			"Flex31": self._Flex31,
			"Flex32": self._Flex32,
			"Div2": self._Div2,
			"FramerFlex2": self._FramerFlex2,
			"Flex33": self._Flex33,
			"footer1": self._footer1,
			"TextBox26": self._TextBox26,
			"TextBox27": self._TextBox27,
			"Flex35": self._Flex35,
			"FramerFlex3": self._FramerFlex3,
			"Flex36": self._Flex36,
			"Flex37": self._Flex37,
			"Flex38": self._Flex38,
			"FramerFlex4": self._FramerFlex4,
			"Div3": self._Div3,
			"Flex40": self._Flex40,
			"TextBox28": self._TextBox28,
			"TextBox29": self._TextBox29,
			"Flex47": self._Flex47,
			"Flex48": self._Flex48,
			"Flex49": self._Flex49,
			"FramerFlex9": self._FramerFlex9,
			"TextBox38": self._TextBox38,
			"TextBox39": self._TextBox39,
			"Flex50": self._Flex50,
			"Div8": self._Div8,
			"TextBox40": self._TextBox40,
			"TextBox41": self._TextBox41,
			"Div9": self._Div9,
			"Flex51": self._Flex51,
			"FramerFlex10": self._FramerFlex10,
			"TextBox42": self._TextBox42,
			"TextBox43": self._TextBox43,
			"Div10": self._Div10,
			"Flex52": self._Flex52,
			"FramerFlex11": self._FramerFlex11,
			"TextBox45": self._TextBox45,
			"Div11": self._Div11,
			"Flex53": self._Flex53,
			"FramerFlex12": self._FramerFlex12,
			"Image10": self._Image10,
			"Flex54": self._Flex54,
			"Flex55": self._Flex55,
			"FramerFlex13": self._FramerFlex13,
			"Flex56": self._Flex56,
			"Div12": self._Div12,
			"TextBox46": self._TextBox46,
			"Flex57": self._Flex57,
			"FramerFlex14": self._FramerFlex14,
			"Anchor62": self._Anchor62,
			"ScaleFlex3": self._ScaleFlex3,
			"Image11": self._Image11,
			"TextBox47": self._TextBox47,
			"TextBox48": self._TextBox48,
			"Image12": self._Image12,
			"ScaleFlex4": self._ScaleFlex4,
			"Anchor63": self._Anchor63,
			"FramerFlex15": self._FramerFlex15,
			"Image13": self._Image13,
			"TextBox49": self._TextBox49,
			"TextBox50": self._TextBox50,
			"Image14": self._Image14,
			"ScaleFlex5": self._ScaleFlex5,
			"ScaleFlex6": self._ScaleFlex6,
			"Anchor64": self._Anchor64,
			"Anchor65": self._Anchor65,
			"FramerFlex16": self._FramerFlex16,
			"FramerFlex17": self._FramerFlex17,
			"Flex58": self._Flex58,
			"Image15": self._Image15,
			"TextBox51": self._TextBox51,
			"TextBox52": self._TextBox52,
			"Image16": self._Image16,
			"ScaleFlex7": self._ScaleFlex7,
			"ScaleFlex8": self._ScaleFlex8,
			"Anchor66": self._Anchor66,
			"Anchor67": self._Anchor67,
			"FramerFlex18": self._FramerFlex18,
			"FramerFlex19": self._FramerFlex19,
			"Flex59": self._Flex59,
			"Image17": self._Image17,
			"TextBox53": self._TextBox53,
			"TextBox54": self._TextBox54,
			"Image18": self._Image18,
			"ScaleFlex9": self._ScaleFlex9,
			"ScaleFlex10": self._ScaleFlex10,
			"Anchor68": self._Anchor68,
			"Anchor69": self._Anchor69,
			"FramerFlex20": self._FramerFlex20,
			"FramerFlex21": self._FramerFlex21,
			"Flex60": self._Flex60,
			"Image19": self._Image19,
			"TextBox55": self._TextBox55,
			"TextBox56": self._TextBox56,
			"Image20": self._Image20,
			"ScaleFlex11": self._ScaleFlex11,
			"ScaleFlex12": self._ScaleFlex12,
			"Anchor70": self._Anchor70,
			"Anchor71": self._Anchor71,
			"FramerFlex22": self._FramerFlex22,
			"FramerFlex23": self._FramerFlex23,
			"Flex61": self._Flex61,
			"Image21": self._Image21,
			"TextBox57": self._TextBox57,
			"TextBox58": self._TextBox58,
			"Image22": self._Image22,
			"ScaleFlex13": self._ScaleFlex13,
			"ScaleFlex14": self._ScaleFlex14,
			"Anchor72": self._Anchor72,
			"Anchor73": self._Anchor73,
			"FramerFlex24": self._FramerFlex24,
			"FramerFlex25": self._FramerFlex25,
			"Flex62": self._Flex62,
			"Image23": self._Image23,
			"TextBox59": self._TextBox59,
			"TextBox60": self._TextBox60,
			"Image24": self._Image24,
			"ScaleFlex15": self._ScaleFlex15,
			"ScaleFlex16": self._ScaleFlex16,
			"Anchor74": self._Anchor74,
			"Anchor75": self._Anchor75,
			"FramerFlex26": self._FramerFlex26,
			"FramerFlex27": self._FramerFlex27,
			"Flex63": self._Flex63,
			"Image25": self._Image25,
			"TextBox61": self._TextBox61,
			"TextBox62": self._TextBox62,
			"Image26": self._Image26,
			"ScaleFlex17": self._ScaleFlex17,
			"ScaleFlex18": self._ScaleFlex18,
			"Anchor76": self._Anchor76,
			"Anchor77": self._Anchor77,
			"FramerFlex28": self._FramerFlex28,
			"FramerFlex29": self._FramerFlex29,
			"Flex64": self._Flex64,
			"Image27": self._Image27,
			"TextBox63": self._TextBox63,
			"TextBox64": self._TextBox64,
			"Image28": self._Image28,
			"ScaleFlex19": self._ScaleFlex19,
			"ScaleFlex20": self._ScaleFlex20,
			"Anchor78": self._Anchor78,
			"Anchor79": self._Anchor79,
			"FramerFlex30": self._FramerFlex30,
			"FramerFlex31": self._FramerFlex31,
			"Flex65": self._Flex65,
			"Image29": self._Image29,
			"TextBox65": self._TextBox65,
			"TextBox66": self._TextBox66,
			"Image30": self._Image30,
			"ScaleFlex21": self._ScaleFlex21,
			"ScaleFlex22": self._ScaleFlex22,
			"Anchor80": self._Anchor80,
			"Anchor81": self._Anchor81,
			"FramerFlex32": self._FramerFlex32,
			"FramerFlex33": self._FramerFlex33,
			"Flex66": self._Flex66,
			"Image31": self._Image31,
			"TextBox67": self._TextBox67,
			"TextBox68": self._TextBox68,
			"Image32": self._Image32,
			"ScaleFlex23": self._ScaleFlex23,
			"ScaleFlex24": self._ScaleFlex24,
			"Anchor82": self._Anchor82,
			"Anchor83": self._Anchor83,
			"FramerFlex34": self._FramerFlex34,
			"FramerFlex35": self._FramerFlex35,
			"Flex67": self._Flex67,
			"Image33": self._Image33,
			"TextBox69": self._TextBox69,
			"TextBox70": self._TextBox70,
			"Image34": self._Image34,
			"ScaleFlex25": self._ScaleFlex25,
			"ScaleFlex26": self._ScaleFlex26,
			"Anchor84": self._Anchor84,
			"Anchor85": self._Anchor85,
			"FramerFlex36": self._FramerFlex36,
			"FramerFlex37": self._FramerFlex37,
			"Flex68": self._Flex68,
			"TextBox71": self._TextBox71,
			"TextBox72": self._TextBox72,
			"ButtonFlex13": self._ButtonFlex13,
			"Anchor86": self._Anchor86,
			"Flex69": self._Flex69,
			"Flex70": self._Flex70,
			"Flex71": self._Flex71,
			"Flex72": self._Flex72,
			"TextBox73": self._TextBox73,
			"Div13": self._Div13,
			"FramerFlex38": self._FramerFlex38,
			"Flex73": self._Flex73,
			"Image35": self._Image35,
			"TextBox74": self._TextBox74,
			"TextBox75": self._TextBox75,
			"Image36": self._Image36,
			"ScaleFlex27": self._ScaleFlex27,
			"ScaleFlex28": self._ScaleFlex28,
			"Anchor87": self._Anchor87,
			"Anchor88": self._Anchor88,
			"FramerFlex39": self._FramerFlex39,
			"FramerFlex40": self._FramerFlex40,
			"Flex74": self._Flex74,
			"Image37": self._Image37,
			"TextBox76": self._TextBox76,
			"TextBox77": self._TextBox77,
			"Image38": self._Image38,
			"ScaleFlex29": self._ScaleFlex29,
			"ScaleFlex30": self._ScaleFlex30,
			"Anchor89": self._Anchor89,
			"Anchor90": self._Anchor90,
			"FramerFlex41": self._FramerFlex41,
			"FramerFlex42": self._FramerFlex42,
			"Flex75": self._Flex75,
			"Image39": self._Image39,
			"TextBox78": self._TextBox78,
			"TextBox79": self._TextBox79,
			"Image40": self._Image40,
			"ScaleFlex31": self._ScaleFlex31,
			"ScaleFlex32": self._ScaleFlex32,
			"Anchor91": self._Anchor91,
			"Anchor92": self._Anchor92,
			"FramerFlex43": self._FramerFlex43,
			"FramerFlex44": self._FramerFlex44,
			"Flex76": self._Flex76,
			"Image41": self._Image41,
			"TextBox80": self._TextBox80,
			"TextBox81": self._TextBox81,
			"Image42": self._Image42,
			"ScaleFlex33": self._ScaleFlex33,
			"ScaleFlex34": self._ScaleFlex34,
			"Anchor93": self._Anchor93,
			"Anchor94": self._Anchor94,
			"FramerFlex45": self._FramerFlex45,
			"FramerFlex46": self._FramerFlex46,
			"Flex77": self._Flex77,
			"TextBox84": self._TextBox84,
			"TextBox85": self._TextBox85,
			"ButtonFlex14": self._ButtonFlex14,
			"Anchor97": self._Anchor97,
			"Flex79": self._Flex79,
			"Flex80": self._Flex80,
			"FramerFlex49": self._FramerFlex49,
			"Flex81": self._Flex81,
			"Flex82": self._Flex82,
			"TextBox86": self._TextBox86,
			"TextBox87": self._TextBox87,
			"TextBox88": self._TextBox88,
			"ButtonFlex15": self._ButtonFlex15,
			"Anchor98": self._Anchor98
			}
  