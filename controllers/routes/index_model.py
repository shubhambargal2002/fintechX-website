from typing import Union, Any
from manifests.ButtonFlex import ButtonFlex
from atri_react.Flex import Flex
from atri_react.TextBox import TextBox
from manifests.ScaleFlex import ScaleFlex
from atri_react.Image import Image
from atri_react.Anchor import Anchor
from manifests.FramerFlex import FramerFlex
from manifests.FramerText import FramerText
from manifests.Pages import Pages
from manifests.DropdownMenu import DropdownMenu
from atri_react.Div import Div
from atri_react.Accordion import Accordion
from manifests.LineText import LineText


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.ButtonFlex1 = state["ButtonFlex1"] if "ButtonFlex1" in state else None
		self.Flex1 = state["Flex1"] if "Flex1" in state else None
		self.Flex2 = state["Flex2"] if "Flex2" in state else None
		self.TextBox2 = state["TextBox2"] if "TextBox2" in state else None
		self.ScaleFlex1 = state["ScaleFlex1"] if "ScaleFlex1" in state else None
		self.Image1 = state["Image1"] if "Image1" in state else None
		self.Flex3 = state["Flex3"] if "Flex3" in state else None
		self.ButtonFlex2 = state["ButtonFlex2"] if "ButtonFlex2" in state else None
		self.TextBox3 = state["TextBox3"] if "TextBox3" in state else None
		self.Anchor1 = state["Anchor1"] if "Anchor1" in state else None
		self.Anchor2 = state["Anchor2"] if "Anchor2" in state else None
		self.Anchor3 = state["Anchor3"] if "Anchor3" in state else None
		self.Flex4 = state["Flex4"] if "Flex4" in state else None
		self.Flex5 = state["Flex5"] if "Flex5" in state else None
		self.FramerFlex1 = state["FramerFlex1"] if "FramerFlex1" in state else None
		self.FramerFlex2 = state["FramerFlex2"] if "FramerFlex2" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.Flex6 = state["Flex6"] if "Flex6" in state else None
		self.Flex7 = state["Flex7"] if "Flex7" in state else None
		self.Flex8 = state["Flex8"] if "Flex8" in state else None
		self.TextBox4 = state["TextBox4"] if "TextBox4" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.ButtonFlex3 = state["ButtonFlex3"] if "ButtonFlex3" in state else None
		self.ButtonFlex4 = state["ButtonFlex4"] if "ButtonFlex4" in state else None
		self.TextBox11 = state["TextBox11"] if "TextBox11" in state else None
		self.Anchor4 = state["Anchor4"] if "Anchor4" in state else None
		self.Anchor5 = state["Anchor5"] if "Anchor5" in state else None
		self.ScaleFlex2 = state["ScaleFlex2"] if "ScaleFlex2" in state else None
		self.TextBox14 = state["TextBox14"] if "TextBox14" in state else None
		self.TextBox15 = state["TextBox15"] if "TextBox15" in state else None
		self.TextBox16 = state["TextBox16"] if "TextBox16" in state else None
		self.TextBox17 = state["TextBox17"] if "TextBox17" in state else None
		self.TextBox18 = state["TextBox18"] if "TextBox18" in state else None
		self.Anchor6 = state["Anchor6"] if "Anchor6" in state else None
		self.Flex9 = state["Flex9"] if "Flex9" in state else None
		self.Anchor7 = state["Anchor7"] if "Anchor7" in state else None
		self.FramerText1 = state["FramerText1"] if "FramerText1" in state else None
		self.FramerText2 = state["FramerText2"] if "FramerText2" in state else None
		self.Anchor8 = state["Anchor8"] if "Anchor8" in state else None
		self.FramerText3 = state["FramerText3"] if "FramerText3" in state else None
		self.Anchor9 = state["Anchor9"] if "Anchor9" in state else None
		self.FramerText4 = state["FramerText4"] if "FramerText4" in state else None
		self.Anchor10 = state["Anchor10"] if "Anchor10" in state else None
		self.Pages1 = state["Pages1"] if "Pages1" in state else None
		self.Flex10 = state["Flex10"] if "Flex10" in state else None
		self.Flex11 = state["Flex11"] if "Flex11" in state else None
		self.DropdownMenu1 = state["DropdownMenu1"] if "DropdownMenu1" in state else None
		self.Flex12 = state["Flex12"] if "Flex12" in state else None
		self.Flex13 = state["Flex13"] if "Flex13" in state else None
		self.Flex14 = state["Flex14"] if "Flex14" in state else None
		self.TextBox19 = state["TextBox19"] if "TextBox19" in state else None
		self.TextBox20 = state["TextBox20"] if "TextBox20" in state else None
		self.TextBox21 = state["TextBox21"] if "TextBox21" in state else None
		self.TextBox22 = state["TextBox22"] if "TextBox22" in state else None
		self.TextBox23 = state["TextBox23"] if "TextBox23" in state else None
		self.Flex15 = state["Flex15"] if "Flex15" in state else None
		self.Flex16 = state["Flex16"] if "Flex16" in state else None
		self.FramerText5 = state["FramerText5"] if "FramerText5" in state else None
		self.Anchor11 = state["Anchor11"] if "Anchor11" in state else None
		self.FramerText6 = state["FramerText6"] if "FramerText6" in state else None
		self.Anchor12 = state["Anchor12"] if "Anchor12" in state else None
		self.FramerText7 = state["FramerText7"] if "FramerText7" in state else None
		self.Anchor13 = state["Anchor13"] if "Anchor13" in state else None
		self.TextBox24 = state["TextBox24"] if "TextBox24" in state else None
		self.TextBox25 = state["TextBox25"] if "TextBox25" in state else None
		self.ButtonFlex5 = state["ButtonFlex5"] if "ButtonFlex5" in state else None
		self.Anchor14 = state["Anchor14"] if "Anchor14" in state else None
		self.Flex17 = state["Flex17"] if "Flex17" in state else None
		self.TextBox28 = state["TextBox28"] if "TextBox28" in state else None
		self.TextBox29 = state["TextBox29"] if "TextBox29" in state else None
		self.ButtonFlex7 = state["ButtonFlex7"] if "ButtonFlex7" in state else None
		self.Anchor16 = state["Anchor16"] if "Anchor16" in state else None
		self.Flex19 = state["Flex19"] if "Flex19" in state else None
		self.Flex20 = state["Flex20"] if "Flex20" in state else None
		self.FramerFlex3 = state["FramerFlex3"] if "FramerFlex3" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.Image4 = state["Image4"] if "Image4" in state else None
		self.Image5 = state["Image5"] if "Image5" in state else None
		self.Image6 = state["Image6"] if "Image6" in state else None
		self.Image7 = state["Image7"] if "Image7" in state else None
		self.Image8 = state["Image8"] if "Image8" in state else None
		self.Flex21 = state["Flex21"] if "Flex21" in state else None
		self.Flex22 = state["Flex22"] if "Flex22" in state else None
		self.FramerFlex4 = state["FramerFlex4"] if "FramerFlex4" in state else None
		self.Flex25 = state["Flex25"] if "Flex25" in state else None
		self.Div1 = state["Div1"] if "Div1" in state else None
		self.TextBox30 = state["TextBox30"] if "TextBox30" in state else None
		self.TextBox31 = state["TextBox31"] if "TextBox31" in state else None
		self.TextBox32 = state["TextBox32"] if "TextBox32" in state else None
		self.TextBox33 = state["TextBox33"] if "TextBox33" in state else None
		self.TextBox34 = state["TextBox34"] if "TextBox34" in state else None
		self.ButtonFlex8 = state["ButtonFlex8"] if "ButtonFlex8" in state else None
		self.ButtonFlex9 = state["ButtonFlex9"] if "ButtonFlex9" in state else None
		self.Anchor17 = state["Anchor17"] if "Anchor17" in state else None
		self.Anchor18 = state["Anchor18"] if "Anchor18" in state else None
		self.Flex26 = state["Flex26"] if "Flex26" in state else None
		self.FramerFlex7 = state["FramerFlex7"] if "FramerFlex7" in state else None
		self.Flex32 = state["Flex32"] if "Flex32" in state else None
		self.Flex33 = state["Flex33"] if "Flex33" in state else None
		self.Flex35 = state["Flex35"] if "Flex35" in state else None
		self.Image9 = state["Image9"] if "Image9" in state else None
		self.Div3 = state["Div3"] if "Div3" in state else None
		self.Flex36 = state["Flex36"] if "Flex36" in state else None
		self.TextBox37 = state["TextBox37"] if "TextBox37" in state else None
		self.TextBox38 = state["TextBox38"] if "TextBox38" in state else None
		self.TextBox39 = state["TextBox39"] if "TextBox39" in state else None
		self.Div4 = state["Div4"] if "Div4" in state else None
		self.TextBox40 = state["TextBox40"] if "TextBox40" in state else None
		self.TextBox41 = state["TextBox41"] if "TextBox41" in state else None
		self.ButtonFlex12 = state["ButtonFlex12"] if "ButtonFlex12" in state else None
		self.Image10 = state["Image10"] if "Image10" in state else None
		self.Anchor21 = state["Anchor21"] if "Anchor21" in state else None
		self.FramerFlex8 = state["FramerFlex8"] if "FramerFlex8" in state else None
		self.Flex37 = state["Flex37"] if "Flex37" in state else None
		self.Flex38 = state["Flex38"] if "Flex38" in state else None
		self.Flex39 = state["Flex39"] if "Flex39" in state else None
		self.Flex40 = state["Flex40"] if "Flex40" in state else None
		self.FramerFlex9 = state["FramerFlex9"] if "FramerFlex9" in state else None
		self.Flex41 = state["Flex41"] if "Flex41" in state else None
		self.Flex42 = state["Flex42"] if "Flex42" in state else None
		self.Flex43 = state["Flex43"] if "Flex43" in state else None
		self.TextBox42 = state["TextBox42"] if "TextBox42" in state else None
		self.TextBox43 = state["TextBox43"] if "TextBox43" in state else None
		self.ButtonFlex13 = state["ButtonFlex13"] if "ButtonFlex13" in state else None
		self.Anchor22 = state["Anchor22"] if "Anchor22" in state else None
		self.Div5 = state["Div5"] if "Div5" in state else None
		self.TextBox44 = state["TextBox44"] if "TextBox44" in state else None
		self.Flex44 = state["Flex44"] if "Flex44" in state else None
		self.Flex45 = state["Flex45"] if "Flex45" in state else None
		self.TextBox45 = state["TextBox45"] if "TextBox45" in state else None
		self.TextBox46 = state["TextBox46"] if "TextBox46" in state else None
		self.Div6 = state["Div6"] if "Div6" in state else None
		self.Div7 = state["Div7"] if "Div7" in state else None
		self.Image11 = state["Image11"] if "Image11" in state else None
		self.Image12 = state["Image12"] if "Image12" in state else None
		self.Image13 = state["Image13"] if "Image13" in state else None
		self.Flex46 = state["Flex46"] if "Flex46" in state else None
		self.Flex47 = state["Flex47"] if "Flex47" in state else None
		self.FramerFlex10 = state["FramerFlex10"] if "FramerFlex10" in state else None
		self.Image14 = state["Image14"] if "Image14" in state else None
		self.Flex50 = state["Flex50"] if "Flex50" in state else None
		self.Flex51 = state["Flex51"] if "Flex51" in state else None
		self.Div8 = state["Div8"] if "Div8" in state else None
		self.TextBox47 = state["TextBox47"] if "TextBox47" in state else None
		self.Flex52 = state["Flex52"] if "Flex52" in state else None
		self.Flex53 = state["Flex53"] if "Flex53" in state else None
		self.Flex54 = state["Flex54"] if "Flex54" in state else None
		self.TextBox48 = state["TextBox48"] if "TextBox48" in state else None
		self.TextBox49 = state["TextBox49"] if "TextBox49" in state else None
		self.TextBox50 = state["TextBox50"] if "TextBox50" in state else None
		self.TextBox51 = state["TextBox51"] if "TextBox51" in state else None
		self.Flex55 = state["Flex55"] if "Flex55" in state else None
		self.TextBox52 = state["TextBox52"] if "TextBox52" in state else None
		self.TextBox53 = state["TextBox53"] if "TextBox53" in state else None
		self.Flex56 = state["Flex56"] if "Flex56" in state else None
		self.TextBox54 = state["TextBox54"] if "TextBox54" in state else None
		self.TextBox55 = state["TextBox55"] if "TextBox55" in state else None
		self.Flex57 = state["Flex57"] if "Flex57" in state else None
		self.Flex58 = state["Flex58"] if "Flex58" in state else None
		self.Flex59 = state["Flex59"] if "Flex59" in state else None
		self.FramerFlex11 = state["FramerFlex11"] if "FramerFlex11" in state else None
		self.FramerFlex12 = state["FramerFlex12"] if "FramerFlex12" in state else None
		self.Div9 = state["Div9"] if "Div9" in state else None
		self.TextBox56 = state["TextBox56"] if "TextBox56" in state else None
		self.Flex60 = state["Flex60"] if "Flex60" in state else None
		self.Flex61 = state["Flex61"] if "Flex61" in state else None
		self.Flex62 = state["Flex62"] if "Flex62" in state else None
		self.Flex63 = state["Flex63"] if "Flex63" in state else None
		self.TextBox57 = state["TextBox57"] if "TextBox57" in state else None
		self.TextBox58 = state["TextBox58"] if "TextBox58" in state else None
		self.TextBox59 = state["TextBox59"] if "TextBox59" in state else None
		self.TextBox60 = state["TextBox60"] if "TextBox60" in state else None
		self.TextBox61 = state["TextBox61"] if "TextBox61" in state else None
		self.TextBox62 = state["TextBox62"] if "TextBox62" in state else None
		self.TextBox63 = state["TextBox63"] if "TextBox63" in state else None
		self.TextBox64 = state["TextBox64"] if "TextBox64" in state else None
		self.Flex64 = state["Flex64"] if "Flex64" in state else None
		self.Flex65 = state["Flex65"] if "Flex65" in state else None
		self.Flex66 = state["Flex66"] if "Flex66" in state else None
		self.TextBox65 = state["TextBox65"] if "TextBox65" in state else None
		self.TextBox66 = state["TextBox66"] if "TextBox66" in state else None
		self.TextBox67 = state["TextBox67"] if "TextBox67" in state else None
		self.TextBox68 = state["TextBox68"] if "TextBox68" in state else None
		self.Flex67 = state["Flex67"] if "Flex67" in state else None
		self.Flex68 = state["Flex68"] if "Flex68" in state else None
		self.Flex69 = state["Flex69"] if "Flex69" in state else None
		self.Image15 = state["Image15"] if "Image15" in state else None
		self.Flex70 = state["Flex70"] if "Flex70" in state else None
		self.ScaleFlex4 = state["ScaleFlex4"] if "ScaleFlex4" in state else None
		self.Image16 = state["Image16"] if "Image16" in state else None
		self.Anchor23 = state["Anchor23"] if "Anchor23" in state else None
		self.Flex71 = state["Flex71"] if "Flex71" in state else None
		self.Flex72 = state["Flex72"] if "Flex72" in state else None
		self.TextBox69 = state["TextBox69"] if "TextBox69" in state else None
		self.TextBox70 = state["TextBox70"] if "TextBox70" in state else None
		self.TextBox71 = state["TextBox71"] if "TextBox71" in state else None
		self.TextBox72 = state["TextBox72"] if "TextBox72" in state else None
		self.ButtonFlex14 = state["ButtonFlex14"] if "ButtonFlex14" in state else None
		self.ButtonFlex15 = state["ButtonFlex15"] if "ButtonFlex15" in state else None
		self.Anchor24 = state["Anchor24"] if "Anchor24" in state else None
		self.Anchor25 = state["Anchor25"] if "Anchor25" in state else None
		self.Flex73 = state["Flex73"] if "Flex73" in state else None
		self.Flex74 = state["Flex74"] if "Flex74" in state else None
		self.FramerFlex13 = state["FramerFlex13"] if "FramerFlex13" in state else None
		self.FramerFlex14 = state["FramerFlex14"] if "FramerFlex14" in state else None
		self.Flex75 = state["Flex75"] if "Flex75" in state else None
		self.TextBox73 = state["TextBox73"] if "TextBox73" in state else None
		self.TextBox74 = state["TextBox74"] if "TextBox74" in state else None
		self.ButtonFlex16 = state["ButtonFlex16"] if "ButtonFlex16" in state else None
		self.Anchor26 = state["Anchor26"] if "Anchor26" in state else None
		self.Div11 = state["Div11"] if "Div11" in state else None
		self.TextBox75 = state["TextBox75"] if "TextBox75" in state else None
		self.Flex76 = state["Flex76"] if "Flex76" in state else None
		self.Flex78 = state["Flex78"] if "Flex78" in state else None
		self.TextBox76 = state["TextBox76"] if "TextBox76" in state else None
		self.Accordion2 = state["Accordion2"] if "Accordion2" in state else None
		self.Accordion3 = state["Accordion3"] if "Accordion3" in state else None
		self.TextBox78 = state["TextBox78"] if "TextBox78" in state else None
		self.Flex79 = state["Flex79"] if "Flex79" in state else None
		self.Flex80 = state["Flex80"] if "Flex80" in state else None
		self.Accordion4 = state["Accordion4"] if "Accordion4" in state else None
		self.TextBox79 = state["TextBox79"] if "TextBox79" in state else None
		self.Flex81 = state["Flex81"] if "Flex81" in state else None
		self.Flex82 = state["Flex82"] if "Flex82" in state else None
		self.Accordion5 = state["Accordion5"] if "Accordion5" in state else None
		self.TextBox80 = state["TextBox80"] if "TextBox80" in state else None
		self.Flex83 = state["Flex83"] if "Flex83" in state else None
		self.Flex84 = state["Flex84"] if "Flex84" in state else None
		self.Flex85 = state["Flex85"] if "Flex85" in state else None
		self.Flex86 = state["Flex86"] if "Flex86" in state else None
		self.FramerFlex15 = state["FramerFlex15"] if "FramerFlex15" in state else None
		self.FramerFlex16 = state["FramerFlex16"] if "FramerFlex16" in state else None
		self.Div12 = state["Div12"] if "Div12" in state else None
		self.TextBox81 = state["TextBox81"] if "TextBox81" in state else None
		self.Image26 = state["Image26"] if "Image26" in state else None
		self.Flex103 = state["Flex103"] if "Flex103" in state else None
		self.TextBox94 = state["TextBox94"] if "TextBox94" in state else None
		self.TextBox95 = state["TextBox95"] if "TextBox95" in state else None
		self.Flex104 = state["Flex104"] if "Flex104" in state else None
		self.TextBox96 = state["TextBox96"] if "TextBox96" in state else None
		self.Div17 = state["Div17"] if "Div17" in state else None
		self.Image27 = state["Image27"] if "Image27" in state else None
		self.Flex105 = state["Flex105"] if "Flex105" in state else None
		self.Flex106 = state["Flex106"] if "Flex106" in state else None
		self.ScaleFlex9 = state["ScaleFlex9"] if "ScaleFlex9" in state else None
		self.Image28 = state["Image28"] if "Image28" in state else None
		self.TextBox97 = state["TextBox97"] if "TextBox97" in state else None
		self.TextBox98 = state["TextBox98"] if "TextBox98" in state else None
		self.Flex107 = state["Flex107"] if "Flex107" in state else None
		self.Image29 = state["Image29"] if "Image29" in state else None
		self.Div18 = state["Div18"] if "Div18" in state else None
		self.TextBox99 = state["TextBox99"] if "TextBox99" in state else None
		self.Flex108 = state["Flex108"] if "Flex108" in state else None
		self.Flex109 = state["Flex109"] if "Flex109" in state else None
		self.Flex110 = state["Flex110"] if "Flex110" in state else None
		self.ScaleFlex10 = state["ScaleFlex10"] if "ScaleFlex10" in state else None
		self.Image30 = state["Image30"] if "Image30" in state else None
		self.TextBox100 = state["TextBox100"] if "TextBox100" in state else None
		self.TextBox101 = state["TextBox101"] if "TextBox101" in state else None
		self.Flex111 = state["Flex111"] if "Flex111" in state else None
		self.Image31 = state["Image31"] if "Image31" in state else None
		self.Div19 = state["Div19"] if "Div19" in state else None
		self.TextBox102 = state["TextBox102"] if "TextBox102" in state else None
		self.Flex112 = state["Flex112"] if "Flex112" in state else None
		self.Flex113 = state["Flex113"] if "Flex113" in state else None
		self.Flex114 = state["Flex114"] if "Flex114" in state else None
		self.ScaleFlex11 = state["ScaleFlex11"] if "ScaleFlex11" in state else None
		self.Anchor33 = state["Anchor33"] if "Anchor33" in state else None
		self.Anchor34 = state["Anchor34"] if "Anchor34" in state else None
		self.Anchor35 = state["Anchor35"] if "Anchor35" in state else None
		self.Image32 = state["Image32"] if "Image32" in state else None
		self.Flex115 = state["Flex115"] if "Flex115" in state else None
		self.TextBox103 = state["TextBox103"] if "TextBox103" in state else None
		self.TextBox104 = state["TextBox104"] if "TextBox104" in state else None
		self.Flex116 = state["Flex116"] if "Flex116" in state else None
		self.TextBox105 = state["TextBox105"] if "TextBox105" in state else None
		self.Div20 = state["Div20"] if "Div20" in state else None
		self.Image33 = state["Image33"] if "Image33" in state else None
		self.Flex117 = state["Flex117"] if "Flex117" in state else None
		self.Flex118 = state["Flex118"] if "Flex118" in state else None
		self.ScaleFlex12 = state["ScaleFlex12"] if "ScaleFlex12" in state else None
		self.Anchor36 = state["Anchor36"] if "Anchor36" in state else None
		self.Image34 = state["Image34"] if "Image34" in state else None
		self.Flex119 = state["Flex119"] if "Flex119" in state else None
		self.TextBox106 = state["TextBox106"] if "TextBox106" in state else None
		self.TextBox107 = state["TextBox107"] if "TextBox107" in state else None
		self.Flex120 = state["Flex120"] if "Flex120" in state else None
		self.TextBox108 = state["TextBox108"] if "TextBox108" in state else None
		self.Div21 = state["Div21"] if "Div21" in state else None
		self.Image35 = state["Image35"] if "Image35" in state else None
		self.Flex121 = state["Flex121"] if "Flex121" in state else None
		self.Flex122 = state["Flex122"] if "Flex122" in state else None
		self.ScaleFlex13 = state["ScaleFlex13"] if "ScaleFlex13" in state else None
		self.Anchor37 = state["Anchor37"] if "Anchor37" in state else None
		self.Image36 = state["Image36"] if "Image36" in state else None
		self.TextBox109 = state["TextBox109"] if "TextBox109" in state else None
		self.TextBox110 = state["TextBox110"] if "TextBox110" in state else None
		self.Flex123 = state["Flex123"] if "Flex123" in state else None
		self.Image37 = state["Image37"] if "Image37" in state else None
		self.Div22 = state["Div22"] if "Div22" in state else None
		self.TextBox111 = state["TextBox111"] if "TextBox111" in state else None
		self.Flex124 = state["Flex124"] if "Flex124" in state else None
		self.Flex125 = state["Flex125"] if "Flex125" in state else None
		self.Flex126 = state["Flex126"] if "Flex126" in state else None
		self.ScaleFlex14 = state["ScaleFlex14"] if "ScaleFlex14" in state else None
		self.Anchor38 = state["Anchor38"] if "Anchor38" in state else None
		self.Flex127 = state["Flex127"] if "Flex127" in state else None
		self.TextBox112 = state["TextBox112"] if "TextBox112" in state else None
		self.TextBox117 = state["TextBox117"] if "TextBox117" in state else None
		self.TextBox118 = state["TextBox118"] if "TextBox118" in state else None
		self.TextBox119 = state["TextBox119"] if "TextBox119" in state else None
		self.TextBox120 = state["TextBox120"] if "TextBox120" in state else None
		self.ButtonFlex19 = state["ButtonFlex19"] if "ButtonFlex19" in state else None
		self.ButtonFlex20 = state["ButtonFlex20"] if "ButtonFlex20" in state else None
		self.Anchor41 = state["Anchor41"] if "Anchor41" in state else None
		self.Anchor42 = state["Anchor42"] if "Anchor42" in state else None
		self.Flex130 = state["Flex130"] if "Flex130" in state else None
		self.Flex131 = state["Flex131"] if "Flex131" in state else None
		self.Flex132 = state["Flex132"] if "Flex132" in state else None
		self.Flex133 = state["Flex133"] if "Flex133" in state else None
		self.FramerFlex17 = state["FramerFlex17"] if "FramerFlex17" in state else None
		self.FramerFlex18 = state["FramerFlex18"] if "FramerFlex18" in state else None
		self.Div23 = state["Div23"] if "Div23" in state else None
		self.Flex134 = state["Flex134"] if "Flex134" in state else None
		self.Flex135 = state["Flex135"] if "Flex135" in state else None
		self.Flex136 = state["Flex136"] if "Flex136" in state else None
		self.Image38 = state["Image38"] if "Image38" in state else None
		self.TextBox121 = state["TextBox121"] if "TextBox121" in state else None
		self.Anchor43 = state["Anchor43"] if "Anchor43" in state else None
		self.ScaleFlex15 = state["ScaleFlex15"] if "ScaleFlex15" in state else None
		self.Flex137 = state["Flex137"] if "Flex137" in state else None
		self.Flex138 = state["Flex138"] if "Flex138" in state else None
		self.Flex139 = state["Flex139"] if "Flex139" in state else None
		self.TextBox122 = state["TextBox122"] if "TextBox122" in state else None
		self.Flex140 = state["Flex140"] if "Flex140" in state else None
		self.Anchor44 = state["Anchor44"] if "Anchor44" in state else None
		self.FramerText8 = state["FramerText8"] if "FramerText8" in state else None
		self.FramerText9 = state["FramerText9"] if "FramerText9" in state else None
		self.Anchor45 = state["Anchor45"] if "Anchor45" in state else None
		self.FramerText10 = state["FramerText10"] if "FramerText10" in state else None
		self.Anchor46 = state["Anchor46"] if "Anchor46" in state else None
		self.FramerText11 = state["FramerText11"] if "FramerText11" in state else None
		self.Anchor47 = state["Anchor47"] if "Anchor47" in state else None
		self.FramerText12 = state["FramerText12"] if "FramerText12" in state else None
		self.Anchor48 = state["Anchor48"] if "Anchor48" in state else None
		self.FramerText13 = state["FramerText13"] if "FramerText13" in state else None
		self.Anchor49 = state["Anchor49"] if "Anchor49" in state else None
		self.FramerText14 = state["FramerText14"] if "FramerText14" in state else None
		self.FramerText15 = state["FramerText15"] if "FramerText15" in state else None
		self.FramerText16 = state["FramerText16"] if "FramerText16" in state else None
		self.FramerText17 = state["FramerText17"] if "FramerText17" in state else None
		self.FramerText18 = state["FramerText18"] if "FramerText18" in state else None
		self.FramerText19 = state["FramerText19"] if "FramerText19" in state else None
		self.Anchor50 = state["Anchor50"] if "Anchor50" in state else None
		self.Anchor51 = state["Anchor51"] if "Anchor51" in state else None
		self.Anchor52 = state["Anchor52"] if "Anchor52" in state else None
		self.Anchor53 = state["Anchor53"] if "Anchor53" in state else None
		self.Anchor54 = state["Anchor54"] if "Anchor54" in state else None
		self.Anchor55 = state["Anchor55"] if "Anchor55" in state else None
		self.Flex141 = state["Flex141"] if "Flex141" in state else None
		self.TextBox123 = state["TextBox123"] if "TextBox123" in state else None
		self.Flex142 = state["Flex142"] if "Flex142" in state else None
		self.FramerText20 = state["FramerText20"] if "FramerText20" in state else None
		self.FramerText21 = state["FramerText21"] if "FramerText21" in state else None
		self.FramerText22 = state["FramerText22"] if "FramerText22" in state else None
		self.FramerText23 = state["FramerText23"] if "FramerText23" in state else None
		self.FramerText24 = state["FramerText24"] if "FramerText24" in state else None
		self.FramerText25 = state["FramerText25"] if "FramerText25" in state else None
		self.Anchor56 = state["Anchor56"] if "Anchor56" in state else None
		self.Anchor57 = state["Anchor57"] if "Anchor57" in state else None
		self.Anchor58 = state["Anchor58"] if "Anchor58" in state else None
		self.Anchor59 = state["Anchor59"] if "Anchor59" in state else None
		self.Anchor60 = state["Anchor60"] if "Anchor60" in state else None
		self.Anchor61 = state["Anchor61"] if "Anchor61" in state else None
		self.Flex143 = state["Flex143"] if "Flex143" in state else None
		self.TextBox124 = state["TextBox124"] if "TextBox124" in state else None
		self.Flex144 = state["Flex144"] if "Flex144" in state else None
		self.Flex145 = state["Flex145"] if "Flex145" in state else None
		self.FramerText26 = state["FramerText26"] if "FramerText26" in state else None
		self.FramerText27 = state["FramerText27"] if "FramerText27" in state else None
		self.FramerText28 = state["FramerText28"] if "FramerText28" in state else None
		self.FramerText29 = state["FramerText29"] if "FramerText29" in state else None
		self.FramerText30 = state["FramerText30"] if "FramerText30" in state else None
		self.FramerText31 = state["FramerText31"] if "FramerText31" in state else None
		self.Anchor62 = state["Anchor62"] if "Anchor62" in state else None
		self.Anchor63 = state["Anchor63"] if "Anchor63" in state else None
		self.Anchor64 = state["Anchor64"] if "Anchor64" in state else None
		self.Anchor65 = state["Anchor65"] if "Anchor65" in state else None
		self.Anchor66 = state["Anchor66"] if "Anchor66" in state else None
		self.Anchor67 = state["Anchor67"] if "Anchor67" in state else None
		self.Flex146 = state["Flex146"] if "Flex146" in state else None
		self.FramerText32 = state["FramerText32"] if "FramerText32" in state else None
		self.Anchor68 = state["Anchor68"] if "Anchor68" in state else None
		self.FramerText33 = state["FramerText33"] if "FramerText33" in state else None
		self.Anchor69 = state["Anchor69"] if "Anchor69" in state else None
		self.FramerText34 = state["FramerText34"] if "FramerText34" in state else None
		self.Anchor70 = state["Anchor70"] if "Anchor70" in state else None
		self.FramerText35 = state["FramerText35"] if "FramerText35" in state else None
		self.Anchor71 = state["Anchor71"] if "Anchor71" in state else None
		self.FramerText36 = state["FramerText36"] if "FramerText36" in state else None
		self.Anchor72 = state["Anchor72"] if "Anchor72" in state else None
		self.FramerText37 = state["FramerText37"] if "FramerText37" in state else None
		self.Anchor73 = state["Anchor73"] if "Anchor73" in state else None
		self.FramerText38 = state["FramerText38"] if "FramerText38" in state else None
		self.Anchor74 = state["Anchor74"] if "Anchor74" in state else None
		self.FramerText39 = state["FramerText39"] if "FramerText39" in state else None
		self.Anchor75 = state["Anchor75"] if "Anchor75" in state else None
		self.FramerText40 = state["FramerText40"] if "FramerText40" in state else None
		self.Anchor76 = state["Anchor76"] if "Anchor76" in state else None
		self.FramerText41 = state["FramerText41"] if "FramerText41" in state else None
		self.Anchor77 = state["Anchor77"] if "Anchor77" in state else None
		self.FramerText42 = state["FramerText42"] if "FramerText42" in state else None
		self.Anchor78 = state["Anchor78"] if "Anchor78" in state else None
		self.Flex147 = state["Flex147"] if "Flex147" in state else None
		self.TextBox125 = state["TextBox125"] if "TextBox125" in state else None
		self.ButtonFlex21 = state["ButtonFlex21"] if "ButtonFlex21" in state else None
		self.Flex148 = state["Flex148"] if "Flex148" in state else None
		self.Anchor79 = state["Anchor79"] if "Anchor79" in state else None
		self.Image39 = state["Image39"] if "Image39" in state else None
		self.Image40 = state["Image40"] if "Image40" in state else None
		self.ButtonFlex22 = state["ButtonFlex22"] if "ButtonFlex22" in state else None
		self.Anchor80 = state["Anchor80"] if "Anchor80" in state else None
		self.Image41 = state["Image41"] if "Image41" in state else None
		self.ButtonFlex23 = state["ButtonFlex23"] if "ButtonFlex23" in state else None
		self.Anchor81 = state["Anchor81"] if "Anchor81" in state else None
		self.Image42 = state["Image42"] if "Image42" in state else None
		self.ButtonFlex24 = state["ButtonFlex24"] if "ButtonFlex24" in state else None
		self.Anchor82 = state["Anchor82"] if "Anchor82" in state else None
		self.Image43 = state["Image43"] if "Image43" in state else None
		self.ButtonFlex25 = state["ButtonFlex25"] if "ButtonFlex25" in state else None
		self.Anchor83 = state["Anchor83"] if "Anchor83" in state else None
		self.Image44 = state["Image44"] if "Image44" in state else None
		self.ButtonFlex26 = state["ButtonFlex26"] if "ButtonFlex26" in state else None
		self.Anchor84 = state["Anchor84"] if "Anchor84" in state else None
		self.Flex149 = state["Flex149"] if "Flex149" in state else None
		self.Div24 = state["Div24"] if "Div24" in state else None
		self.Flex150 = state["Flex150"] if "Flex150" in state else None
		self.TextBox132 = state["TextBox132"] if "TextBox132" in state else None
		self.Anchor85 = state["Anchor85"] if "Anchor85" in state else None
		self.TextBox134 = state["TextBox134"] if "TextBox134" in state else None
		self.FramerText43 = state["FramerText43"] if "FramerText43" in state else None
		self.FramerText44 = state["FramerText44"] if "FramerText44" in state else None
		self.Anchor87 = state["Anchor87"] if "Anchor87" in state else None
		self.TextBox136 = state["TextBox136"] if "TextBox136" in state else None
		self.Image45 = state["Image45"] if "Image45" in state else None
		self.Anchor88 = state["Anchor88"] if "Anchor88" in state else None
		self.TextBox137 = state["TextBox137"] if "TextBox137" in state else None
		self.TextBox138 = state["TextBox138"] if "TextBox138" in state else None
		self.TextBox139 = state["TextBox139"] if "TextBox139" in state else None
		self.TextBox140 = state["TextBox140"] if "TextBox140" in state else None
		self.TextBox141 = state["TextBox141"] if "TextBox141" in state else None
		self.TextBox142 = state["TextBox142"] if "TextBox142" in state else None
		self.LineText1 = state["LineText1"] if "LineText1" in state else None
		self.LineText2 = state["LineText2"] if "LineText2" in state else None
		self.Anchor89 = state["Anchor89"] if "Anchor89" in state else None
		self.Anchor90 = state["Anchor90"] if "Anchor90" in state else None
		self.ButtonFlex27 = state["ButtonFlex27"] if "ButtonFlex27" in state else None
		self.Flex151 = state["Flex151"] if "Flex151" in state else None
		self.Flex152 = state["Flex152"] if "Flex152" in state else None
		self.TextBox143 = state["TextBox143"] if "TextBox143" in state else None
		self.Flex153 = state["Flex153"] if "Flex153" in state else None
		self.TextBox144 = state["TextBox144"] if "TextBox144" in state else None
		self.TextBox145 = state["TextBox145"] if "TextBox145" in state else None
		self.Flex154 = state["Flex154"] if "Flex154" in state else None
		self.Image46 = state["Image46"] if "Image46" in state else None
		self.TextBox146 = state["TextBox146"] if "TextBox146" in state else None
		self.TextBox147 = state["TextBox147"] if "TextBox147" in state else None
		self.Image47 = state["Image47"] if "Image47" in state else None
		self.Flex155 = state["Flex155"] if "Flex155" in state else None
		self.TextBox148 = state["TextBox148"] if "TextBox148" in state else None
		self.Flex156 = state["Flex156"] if "Flex156" in state else None
		self.Flex157 = state["Flex157"] if "Flex157" in state else None
		self.Flex158 = state["Flex158"] if "Flex158" in state else None
		self.ButtonFlex28 = state["ButtonFlex28"] if "ButtonFlex28" in state else None
		self.Anchor91 = state["Anchor91"] if "Anchor91" in state else None
		self.Flex159 = state["Flex159"] if "Flex159" in state else None
		self.FramerFlex19 = state["FramerFlex19"] if "FramerFlex19" in state else None
		self.TextBox149 = state["TextBox149"] if "TextBox149" in state else None
		self.TextBox150 = state["TextBox150"] if "TextBox150" in state else None
		self.Image48 = state["Image48"] if "Image48" in state else None
		self.Flex161 = state["Flex161"] if "Flex161" in state else None
		self.TextBox151 = state["TextBox151"] if "TextBox151" in state else None
		self.Flex162 = state["Flex162"] if "Flex162" in state else None
		self.Flex163 = state["Flex163"] if "Flex163" in state else None
		self.Flex164 = state["Flex164"] if "Flex164" in state else None
		self.ButtonFlex29 = state["ButtonFlex29"] if "ButtonFlex29" in state else None
		self.Anchor92 = state["Anchor92"] if "Anchor92" in state else None
		self.TextBox152 = state["TextBox152"] if "TextBox152" in state else None
		self.TextBox153 = state["TextBox153"] if "TextBox153" in state else None
		self.Image49 = state["Image49"] if "Image49" in state else None
		self.Flex165 = state["Flex165"] if "Flex165" in state else None
		self.TextBox154 = state["TextBox154"] if "TextBox154" in state else None
		self.Flex166 = state["Flex166"] if "Flex166" in state else None
		self.Flex167 = state["Flex167"] if "Flex167" in state else None
		self.Flex168 = state["Flex168"] if "Flex168" in state else None
		self.ButtonFlex30 = state["ButtonFlex30"] if "ButtonFlex30" in state else None
		self.Anchor93 = state["Anchor93"] if "Anchor93" in state else None
		self.TextBox155 = state["TextBox155"] if "TextBox155" in state else None
		self.TextBox156 = state["TextBox156"] if "TextBox156" in state else None
		self.Image50 = state["Image50"] if "Image50" in state else None
		self.Flex169 = state["Flex169"] if "Flex169" in state else None
		self.TextBox157 = state["TextBox157"] if "TextBox157" in state else None
		self.Flex170 = state["Flex170"] if "Flex170" in state else None
		self.Flex171 = state["Flex171"] if "Flex171" in state else None
		self.Flex172 = state["Flex172"] if "Flex172" in state else None
		self.ButtonFlex31 = state["ButtonFlex31"] if "ButtonFlex31" in state else None
		self.Anchor94 = state["Anchor94"] if "Anchor94" in state else None
		self.Anchor95 = state["Anchor95"] if "Anchor95" in state else None
		self.LineText3 = state["LineText3"] if "LineText3" in state else None
		self.FramerFlex20 = state["FramerFlex20"] if "FramerFlex20" in state else None
		self.FramerFlex21 = state["FramerFlex21"] if "FramerFlex21" in state else None
		self.FramerText46 = state["FramerText46"] if "FramerText46" in state else None
		self.FramerText47 = state["FramerText47"] if "FramerText47" in state else None
		self.FramerText48 = state["FramerText48"] if "FramerText48" in state else None
		self.FramerText49 = state["FramerText49"] if "FramerText49" in state else None
		self.FramerText50 = state["FramerText50"] if "FramerText50" in state else None
		self.FramerText51 = state["FramerText51"] if "FramerText51" in state else None
		self.FramerText52 = state["FramerText52"] if "FramerText52" in state else None
		self.FramerText53 = state["FramerText53"] if "FramerText53" in state else None
		self.FramerText54 = state["FramerText54"] if "FramerText54" in state else None
		self.FramerText55 = state["FramerText55"] if "FramerText55" in state else None
		self.FramerText56 = state["FramerText56"] if "FramerText56" in state else None
		self.FramerText57 = state["FramerText57"] if "FramerText57" in state else None
		self.FramerText58 = state["FramerText58"] if "FramerText58" in state else None
		self.FramerText59 = state["FramerText59"] if "FramerText59" in state else None
		self.FramerText60 = state["FramerText60"] if "FramerText60" in state else None
		self.FramerText61 = state["FramerText61"] if "FramerText61" in state else None
		self.FramerText62 = state["FramerText62"] if "FramerText62" in state else None
		self.FramerText63 = state["FramerText63"] if "FramerText63" in state else None
		self.FramerText64 = state["FramerText64"] if "FramerText64" in state else None
		self.FramerText65 = state["FramerText65"] if "FramerText65" in state else None
		self.FramerText66 = state["FramerText66"] if "FramerText66" in state else None
		self.FramerText67 = state["FramerText67"] if "FramerText67" in state else None
		self.FramerText68 = state["FramerText68"] if "FramerText68" in state else None
		self.Anchor97 = state["Anchor97"] if "Anchor97" in state else None
		self.Anchor98 = state["Anchor98"] if "Anchor98" in state else None
		self.Anchor99 = state["Anchor99"] if "Anchor99" in state else None
		self.Anchor100 = state["Anchor100"] if "Anchor100" in state else None
		self.Anchor101 = state["Anchor101"] if "Anchor101" in state else None
		self.Anchor102 = state["Anchor102"] if "Anchor102" in state else None
		self.Anchor103 = state["Anchor103"] if "Anchor103" in state else None
		self.Anchor104 = state["Anchor104"] if "Anchor104" in state else None
		self.Anchor105 = state["Anchor105"] if "Anchor105" in state else None
		self.Anchor106 = state["Anchor106"] if "Anchor106" in state else None
		self.Anchor107 = state["Anchor107"] if "Anchor107" in state else None
		self.Anchor108 = state["Anchor108"] if "Anchor108" in state else None
		self.Anchor109 = state["Anchor109"] if "Anchor109" in state else None
		self.Anchor110 = state["Anchor110"] if "Anchor110" in state else None
		self.Anchor111 = state["Anchor111"] if "Anchor111" in state else None
		self.Anchor112 = state["Anchor112"] if "Anchor112" in state else None
		self.Anchor113 = state["Anchor113"] if "Anchor113" in state else None
		self.Anchor114 = state["Anchor114"] if "Anchor114" in state else None
		self.Anchor115 = state["Anchor115"] if "Anchor115" in state else None
		self.Anchor116 = state["Anchor116"] if "Anchor116" in state else None
		self.Anchor117 = state["Anchor117"] if "Anchor117" in state else None
		self.Anchor118 = state["Anchor118"] if "Anchor118" in state else None
		self.Anchor119 = state["Anchor119"] if "Anchor119" in state else None
		self.Flex173 = state["Flex173"] if "Flex173" in state else None
		self.Flex174 = state["Flex174"] if "Flex174" in state else None
		self.Flex175 = state["Flex175"] if "Flex175" in state else None
		self.TextBox158 = state["TextBox158"] if "TextBox158" in state else None
		self.Flex176 = state["Flex176"] if "Flex176" in state else None
		self.FramerText69 = state["FramerText69"] if "FramerText69" in state else None
		self.FramerText70 = state["FramerText70"] if "FramerText70" in state else None
		self.FramerText71 = state["FramerText71"] if "FramerText71" in state else None
		self.FramerText72 = state["FramerText72"] if "FramerText72" in state else None
		self.FramerText73 = state["FramerText73"] if "FramerText73" in state else None
		self.FramerText74 = state["FramerText74"] if "FramerText74" in state else None
		self.Anchor120 = state["Anchor120"] if "Anchor120" in state else None
		self.Anchor121 = state["Anchor121"] if "Anchor121" in state else None
		self.Anchor122 = state["Anchor122"] if "Anchor122" in state else None
		self.Anchor123 = state["Anchor123"] if "Anchor123" in state else None
		self.Anchor124 = state["Anchor124"] if "Anchor124" in state else None
		self.Anchor125 = state["Anchor125"] if "Anchor125" in state else None
		self.TextBox159 = state["TextBox159"] if "TextBox159" in state else None
		self.Flex177 = state["Flex177"] if "Flex177" in state else None
		self.Flex178 = state["Flex178"] if "Flex178" in state else None
		self.Flex179 = state["Flex179"] if "Flex179" in state else None
		self.LineText4 = state["LineText4"] if "LineText4" in state else None
		self.FramerText75 = state["FramerText75"] if "FramerText75" in state else None
		self.FramerText76 = state["FramerText76"] if "FramerText76" in state else None
		self.FramerText77 = state["FramerText77"] if "FramerText77" in state else None
		self.FramerText78 = state["FramerText78"] if "FramerText78" in state else None
		self.FramerText79 = state["FramerText79"] if "FramerText79" in state else None
		self.FramerText80 = state["FramerText80"] if "FramerText80" in state else None
		self.Anchor126 = state["Anchor126"] if "Anchor126" in state else None
		self.Anchor127 = state["Anchor127"] if "Anchor127" in state else None
		self.Anchor128 = state["Anchor128"] if "Anchor128" in state else None
		self.Anchor129 = state["Anchor129"] if "Anchor129" in state else None
		self.Anchor130 = state["Anchor130"] if "Anchor130" in state else None
		self.Anchor131 = state["Anchor131"] if "Anchor131" in state else None
		self.Anchor132 = state["Anchor132"] if "Anchor132" in state else None
		self.TextBox160 = state["TextBox160"] if "TextBox160" in state else None
		self.Flex180 = state["Flex180"] if "Flex180" in state else None
		self.Flex181 = state["Flex181"] if "Flex181" in state else None
		self.FramerText81 = state["FramerText81"] if "FramerText81" in state else None
		self.FramerText82 = state["FramerText82"] if "FramerText82" in state else None
		self.FramerText83 = state["FramerText83"] if "FramerText83" in state else None
		self.FramerText84 = state["FramerText84"] if "FramerText84" in state else None
		self.FramerText85 = state["FramerText85"] if "FramerText85" in state else None
		self.FramerText86 = state["FramerText86"] if "FramerText86" in state else None
		self.LineText5 = state["LineText5"] if "LineText5" in state else None
		self.FramerText87 = state["FramerText87"] if "FramerText87" in state else None
		self.FramerText88 = state["FramerText88"] if "FramerText88" in state else None
		self.FramerText89 = state["FramerText89"] if "FramerText89" in state else None
		self.FramerText90 = state["FramerText90"] if "FramerText90" in state else None
		self.FramerText91 = state["FramerText91"] if "FramerText91" in state else None
		self.FramerText92 = state["FramerText92"] if "FramerText92" in state else None
		self.FramerText93 = state["FramerText93"] if "FramerText93" in state else None
		self.FramerText94 = state["FramerText94"] if "FramerText94" in state else None
		self.FramerText95 = state["FramerText95"] if "FramerText95" in state else None
		self.FramerText96 = state["FramerText96"] if "FramerText96" in state else None
		self.FramerText97 = state["FramerText97"] if "FramerText97" in state else None
		self.FramerText98 = state["FramerText98"] if "FramerText98" in state else None
		self.FramerText99 = state["FramerText99"] if "FramerText99" in state else None
		self.FramerText100 = state["FramerText100"] if "FramerText100" in state else None
		self.FramerText101 = state["FramerText101"] if "FramerText101" in state else None
		self.FramerText102 = state["FramerText102"] if "FramerText102" in state else None
		self.FramerText103 = state["FramerText103"] if "FramerText103" in state else None
		self.FramerText104 = state["FramerText104"] if "FramerText104" in state else None
		self.FramerText105 = state["FramerText105"] if "FramerText105" in state else None
		self.FramerText106 = state["FramerText106"] if "FramerText106" in state else None
		self.FramerText107 = state["FramerText107"] if "FramerText107" in state else None
		self.FramerText108 = state["FramerText108"] if "FramerText108" in state else None
		self.FramerText109 = state["FramerText109"] if "FramerText109" in state else None
		self.FramerText110 = state["FramerText110"] if "FramerText110" in state else None
		self.FramerText111 = state["FramerText111"] if "FramerText111" in state else None
		self.FramerText112 = state["FramerText112"] if "FramerText112" in state else None
		self.FramerText113 = state["FramerText113"] if "FramerText113" in state else None
		self.FramerText114 = state["FramerText114"] if "FramerText114" in state else None
		self.FramerText115 = state["FramerText115"] if "FramerText115" in state else None
		self.Anchor133 = state["Anchor133"] if "Anchor133" in state else None
		self.Anchor134 = state["Anchor134"] if "Anchor134" in state else None
		self.Anchor135 = state["Anchor135"] if "Anchor135" in state else None
		self.Anchor136 = state["Anchor136"] if "Anchor136" in state else None
		self.Anchor137 = state["Anchor137"] if "Anchor137" in state else None
		self.Anchor138 = state["Anchor138"] if "Anchor138" in state else None
		self.Anchor139 = state["Anchor139"] if "Anchor139" in state else None
		self.Anchor140 = state["Anchor140"] if "Anchor140" in state else None
		self.Anchor141 = state["Anchor141"] if "Anchor141" in state else None
		self.Anchor142 = state["Anchor142"] if "Anchor142" in state else None
		self.Anchor143 = state["Anchor143"] if "Anchor143" in state else None
		self.Anchor144 = state["Anchor144"] if "Anchor144" in state else None
		self.Anchor145 = state["Anchor145"] if "Anchor145" in state else None
		self.Anchor146 = state["Anchor146"] if "Anchor146" in state else None
		self.Anchor147 = state["Anchor147"] if "Anchor147" in state else None
		self.Anchor148 = state["Anchor148"] if "Anchor148" in state else None
		self.Anchor149 = state["Anchor149"] if "Anchor149" in state else None
		self.Anchor150 = state["Anchor150"] if "Anchor150" in state else None
		self.Anchor151 = state["Anchor151"] if "Anchor151" in state else None
		self.Anchor152 = state["Anchor152"] if "Anchor152" in state else None
		self.Anchor153 = state["Anchor153"] if "Anchor153" in state else None
		self.Anchor154 = state["Anchor154"] if "Anchor154" in state else None
		self.Anchor155 = state["Anchor155"] if "Anchor155" in state else None
		self.Anchor156 = state["Anchor156"] if "Anchor156" in state else None
		self.Anchor157 = state["Anchor157"] if "Anchor157" in state else None
		self.Anchor158 = state["Anchor158"] if "Anchor158" in state else None
		self.Anchor159 = state["Anchor159"] if "Anchor159" in state else None
		self.Anchor160 = state["Anchor160"] if "Anchor160" in state else None
		self.Anchor161 = state["Anchor161"] if "Anchor161" in state else None
		self.Anchor162 = state["Anchor162"] if "Anchor162" in state else None
		self.Anchor163 = state["Anchor163"] if "Anchor163" in state else None
		self.Anchor164 = state["Anchor164"] if "Anchor164" in state else None
		self.Anchor165 = state["Anchor165"] if "Anchor165" in state else None
		self.Anchor166 = state["Anchor166"] if "Anchor166" in state else None
		self.Anchor167 = state["Anchor167"] if "Anchor167" in state else None
		self.Anchor168 = state["Anchor168"] if "Anchor168" in state else None
		self.Flex182 = state["Flex182"] if "Flex182" in state else None
		self.TextBox161 = state["TextBox161"] if "TextBox161" in state else None
		self.Flex183 = state["Flex183"] if "Flex183" in state else None
		self.TextBox162 = state["TextBox162"] if "TextBox162" in state else None
		self.Flex184 = state["Flex184"] if "Flex184" in state else None
		self.Flex185 = state["Flex185"] if "Flex185" in state else None
		self.Flex186 = state["Flex186"] if "Flex186" in state else None
		self.Flex187 = state["Flex187"] if "Flex187" in state else None
		self.TextBox163 = state["TextBox163"] if "TextBox163" in state else None
		self.Flex188 = state["Flex188"] if "Flex188" in state else None
		self.Flex189 = state["Flex189"] if "Flex189" in state else None
		self.Flex190 = state["Flex190"] if "Flex190" in state else None
		self.Flex191 = state["Flex191"] if "Flex191" in state else None
		self.Pages2 = state["Pages2"] if "Pages2" in state else None
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
	def ButtonFlex1(self):
		self._getter_access_tracker["ButtonFlex1"] = {}
		return self._ButtonFlex1
	@ButtonFlex1.setter
	def ButtonFlex1(self, new_state):
		self._setter_access_tracker["ButtonFlex1"] = {}
		self._ButtonFlex1 = ButtonFlex(new_state)

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
	def TextBox2(self):
		self._getter_access_tracker["TextBox2"] = {}
		return self._TextBox2
	@TextBox2.setter
	def TextBox2(self, new_state):
		self._setter_access_tracker["TextBox2"] = {}
		self._TextBox2 = TextBox(new_state)

	@property
	def ScaleFlex1(self):
		self._getter_access_tracker["ScaleFlex1"] = {}
		return self._ScaleFlex1
	@ScaleFlex1.setter
	def ScaleFlex1(self, new_state):
		self._setter_access_tracker["ScaleFlex1"] = {}
		self._ScaleFlex1 = ScaleFlex(new_state)

	@property
	def Image1(self):
		self._getter_access_tracker["Image1"] = {}
		return self._Image1
	@Image1.setter
	def Image1(self, new_state):
		self._setter_access_tracker["Image1"] = {}
		self._Image1 = Image(new_state)

	@property
	def Flex3(self):
		self._getter_access_tracker["Flex3"] = {}
		return self._Flex3
	@Flex3.setter
	def Flex3(self, new_state):
		self._setter_access_tracker["Flex3"] = {}
		self._Flex3 = Flex(new_state)

	@property
	def ButtonFlex2(self):
		self._getter_access_tracker["ButtonFlex2"] = {}
		return self._ButtonFlex2
	@ButtonFlex2.setter
	def ButtonFlex2(self, new_state):
		self._setter_access_tracker["ButtonFlex2"] = {}
		self._ButtonFlex2 = ButtonFlex(new_state)

	@property
	def TextBox3(self):
		self._getter_access_tracker["TextBox3"] = {}
		return self._TextBox3
	@TextBox3.setter
	def TextBox3(self, new_state):
		self._setter_access_tracker["TextBox3"] = {}
		self._TextBox3 = TextBox(new_state)

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
	def Anchor3(self):
		self._getter_access_tracker["Anchor3"] = {}
		return self._Anchor3
	@Anchor3.setter
	def Anchor3(self, new_state):
		self._setter_access_tracker["Anchor3"] = {}
		self._Anchor3 = Anchor(new_state)

	@property
	def Flex4(self):
		self._getter_access_tracker["Flex4"] = {}
		return self._Flex4
	@Flex4.setter
	def Flex4(self, new_state):
		self._setter_access_tracker["Flex4"] = {}
		self._Flex4 = Flex(new_state)

	@property
	def Flex5(self):
		self._getter_access_tracker["Flex5"] = {}
		return self._Flex5
	@Flex5.setter
	def Flex5(self, new_state):
		self._setter_access_tracker["Flex5"] = {}
		self._Flex5 = Flex(new_state)

	@property
	def FramerFlex1(self):
		self._getter_access_tracker["FramerFlex1"] = {}
		return self._FramerFlex1
	@FramerFlex1.setter
	def FramerFlex1(self, new_state):
		self._setter_access_tracker["FramerFlex1"] = {}
		self._FramerFlex1 = FramerFlex(new_state)

	@property
	def FramerFlex2(self):
		self._getter_access_tracker["FramerFlex2"] = {}
		return self._FramerFlex2
	@FramerFlex2.setter
	def FramerFlex2(self, new_state):
		self._setter_access_tracker["FramerFlex2"] = {}
		self._FramerFlex2 = FramerFlex(new_state)

	@property
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

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
	def TextBox4(self):
		self._getter_access_tracker["TextBox4"] = {}
		return self._TextBox4
	@TextBox4.setter
	def TextBox4(self, new_state):
		self._setter_access_tracker["TextBox4"] = {}
		self._TextBox4 = TextBox(new_state)

	@property
	def TextBox10(self):
		self._getter_access_tracker["TextBox10"] = {}
		return self._TextBox10
	@TextBox10.setter
	def TextBox10(self, new_state):
		self._setter_access_tracker["TextBox10"] = {}
		self._TextBox10 = TextBox(new_state)

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
	def TextBox11(self):
		self._getter_access_tracker["TextBox11"] = {}
		return self._TextBox11
	@TextBox11.setter
	def TextBox11(self, new_state):
		self._setter_access_tracker["TextBox11"] = {}
		self._TextBox11 = TextBox(new_state)

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
	def ScaleFlex2(self):
		self._getter_access_tracker["ScaleFlex2"] = {}
		return self._ScaleFlex2
	@ScaleFlex2.setter
	def ScaleFlex2(self, new_state):
		self._setter_access_tracker["ScaleFlex2"] = {}
		self._ScaleFlex2 = ScaleFlex(new_state)

	@property
	def TextBox14(self):
		self._getter_access_tracker["TextBox14"] = {}
		return self._TextBox14
	@TextBox14.setter
	def TextBox14(self, new_state):
		self._setter_access_tracker["TextBox14"] = {}
		self._TextBox14 = TextBox(new_state)

	@property
	def TextBox15(self):
		self._getter_access_tracker["TextBox15"] = {}
		return self._TextBox15
	@TextBox15.setter
	def TextBox15(self, new_state):
		self._setter_access_tracker["TextBox15"] = {}
		self._TextBox15 = TextBox(new_state)

	@property
	def TextBox16(self):
		self._getter_access_tracker["TextBox16"] = {}
		return self._TextBox16
	@TextBox16.setter
	def TextBox16(self, new_state):
		self._setter_access_tracker["TextBox16"] = {}
		self._TextBox16 = TextBox(new_state)

	@property
	def TextBox17(self):
		self._getter_access_tracker["TextBox17"] = {}
		return self._TextBox17
	@TextBox17.setter
	def TextBox17(self, new_state):
		self._setter_access_tracker["TextBox17"] = {}
		self._TextBox17 = TextBox(new_state)

	@property
	def TextBox18(self):
		self._getter_access_tracker["TextBox18"] = {}
		return self._TextBox18
	@TextBox18.setter
	def TextBox18(self, new_state):
		self._setter_access_tracker["TextBox18"] = {}
		self._TextBox18 = TextBox(new_state)

	@property
	def Anchor6(self):
		self._getter_access_tracker["Anchor6"] = {}
		return self._Anchor6
	@Anchor6.setter
	def Anchor6(self, new_state):
		self._setter_access_tracker["Anchor6"] = {}
		self._Anchor6 = Anchor(new_state)

	@property
	def Flex9(self):
		self._getter_access_tracker["Flex9"] = {}
		return self._Flex9
	@Flex9.setter
	def Flex9(self, new_state):
		self._setter_access_tracker["Flex9"] = {}
		self._Flex9 = Flex(new_state)

	@property
	def Anchor7(self):
		self._getter_access_tracker["Anchor7"] = {}
		return self._Anchor7
	@Anchor7.setter
	def Anchor7(self, new_state):
		self._setter_access_tracker["Anchor7"] = {}
		self._Anchor7 = Anchor(new_state)

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
	def Anchor8(self):
		self._getter_access_tracker["Anchor8"] = {}
		return self._Anchor8
	@Anchor8.setter
	def Anchor8(self, new_state):
		self._setter_access_tracker["Anchor8"] = {}
		self._Anchor8 = Anchor(new_state)

	@property
	def FramerText3(self):
		self._getter_access_tracker["FramerText3"] = {}
		return self._FramerText3
	@FramerText3.setter
	def FramerText3(self, new_state):
		self._setter_access_tracker["FramerText3"] = {}
		self._FramerText3 = FramerText(new_state)

	@property
	def Anchor9(self):
		self._getter_access_tracker["Anchor9"] = {}
		return self._Anchor9
	@Anchor9.setter
	def Anchor9(self, new_state):
		self._setter_access_tracker["Anchor9"] = {}
		self._Anchor9 = Anchor(new_state)

	@property
	def FramerText4(self):
		self._getter_access_tracker["FramerText4"] = {}
		return self._FramerText4
	@FramerText4.setter
	def FramerText4(self, new_state):
		self._setter_access_tracker["FramerText4"] = {}
		self._FramerText4 = FramerText(new_state)

	@property
	def Anchor10(self):
		self._getter_access_tracker["Anchor10"] = {}
		return self._Anchor10
	@Anchor10.setter
	def Anchor10(self, new_state):
		self._setter_access_tracker["Anchor10"] = {}
		self._Anchor10 = Anchor(new_state)

	@property
	def Pages1(self):
		self._getter_access_tracker["Pages1"] = {}
		return self._Pages1
	@Pages1.setter
	def Pages1(self, new_state):
		self._setter_access_tracker["Pages1"] = {}
		self._Pages1 = Pages(new_state)

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
	def DropdownMenu1(self):
		self._getter_access_tracker["DropdownMenu1"] = {}
		return self._DropdownMenu1
	@DropdownMenu1.setter
	def DropdownMenu1(self, new_state):
		self._setter_access_tracker["DropdownMenu1"] = {}
		self._DropdownMenu1 = DropdownMenu(new_state)

	@property
	def Flex12(self):
		self._getter_access_tracker["Flex12"] = {}
		return self._Flex12
	@Flex12.setter
	def Flex12(self, new_state):
		self._setter_access_tracker["Flex12"] = {}
		self._Flex12 = Flex(new_state)

	@property
	def Flex13(self):
		self._getter_access_tracker["Flex13"] = {}
		return self._Flex13
	@Flex13.setter
	def Flex13(self, new_state):
		self._setter_access_tracker["Flex13"] = {}
		self._Flex13 = Flex(new_state)

	@property
	def Flex14(self):
		self._getter_access_tracker["Flex14"] = {}
		return self._Flex14
	@Flex14.setter
	def Flex14(self, new_state):
		self._setter_access_tracker["Flex14"] = {}
		self._Flex14 = Flex(new_state)

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
	def TextBox21(self):
		self._getter_access_tracker["TextBox21"] = {}
		return self._TextBox21
	@TextBox21.setter
	def TextBox21(self, new_state):
		self._setter_access_tracker["TextBox21"] = {}
		self._TextBox21 = TextBox(new_state)

	@property
	def TextBox22(self):
		self._getter_access_tracker["TextBox22"] = {}
		return self._TextBox22
	@TextBox22.setter
	def TextBox22(self, new_state):
		self._setter_access_tracker["TextBox22"] = {}
		self._TextBox22 = TextBox(new_state)

	@property
	def TextBox23(self):
		self._getter_access_tracker["TextBox23"] = {}
		return self._TextBox23
	@TextBox23.setter
	def TextBox23(self, new_state):
		self._setter_access_tracker["TextBox23"] = {}
		self._TextBox23 = TextBox(new_state)

	@property
	def Flex15(self):
		self._getter_access_tracker["Flex15"] = {}
		return self._Flex15
	@Flex15.setter
	def Flex15(self, new_state):
		self._setter_access_tracker["Flex15"] = {}
		self._Flex15 = Flex(new_state)

	@property
	def Flex16(self):
		self._getter_access_tracker["Flex16"] = {}
		return self._Flex16
	@Flex16.setter
	def Flex16(self, new_state):
		self._setter_access_tracker["Flex16"] = {}
		self._Flex16 = Flex(new_state)

	@property
	def FramerText5(self):
		self._getter_access_tracker["FramerText5"] = {}
		return self._FramerText5
	@FramerText5.setter
	def FramerText5(self, new_state):
		self._setter_access_tracker["FramerText5"] = {}
		self._FramerText5 = FramerText(new_state)

	@property
	def Anchor11(self):
		self._getter_access_tracker["Anchor11"] = {}
		return self._Anchor11
	@Anchor11.setter
	def Anchor11(self, new_state):
		self._setter_access_tracker["Anchor11"] = {}
		self._Anchor11 = Anchor(new_state)

	@property
	def FramerText6(self):
		self._getter_access_tracker["FramerText6"] = {}
		return self._FramerText6
	@FramerText6.setter
	def FramerText6(self, new_state):
		self._setter_access_tracker["FramerText6"] = {}
		self._FramerText6 = FramerText(new_state)

	@property
	def Anchor12(self):
		self._getter_access_tracker["Anchor12"] = {}
		return self._Anchor12
	@Anchor12.setter
	def Anchor12(self, new_state):
		self._setter_access_tracker["Anchor12"] = {}
		self._Anchor12 = Anchor(new_state)

	@property
	def FramerText7(self):
		self._getter_access_tracker["FramerText7"] = {}
		return self._FramerText7
	@FramerText7.setter
	def FramerText7(self, new_state):
		self._setter_access_tracker["FramerText7"] = {}
		self._FramerText7 = FramerText(new_state)

	@property
	def Anchor13(self):
		self._getter_access_tracker["Anchor13"] = {}
		return self._Anchor13
	@Anchor13.setter
	def Anchor13(self, new_state):
		self._setter_access_tracker["Anchor13"] = {}
		self._Anchor13 = Anchor(new_state)

	@property
	def TextBox24(self):
		self._getter_access_tracker["TextBox24"] = {}
		return self._TextBox24
	@TextBox24.setter
	def TextBox24(self, new_state):
		self._setter_access_tracker["TextBox24"] = {}
		self._TextBox24 = TextBox(new_state)

	@property
	def TextBox25(self):
		self._getter_access_tracker["TextBox25"] = {}
		return self._TextBox25
	@TextBox25.setter
	def TextBox25(self, new_state):
		self._setter_access_tracker["TextBox25"] = {}
		self._TextBox25 = TextBox(new_state)

	@property
	def ButtonFlex5(self):
		self._getter_access_tracker["ButtonFlex5"] = {}
		return self._ButtonFlex5
	@ButtonFlex5.setter
	def ButtonFlex5(self, new_state):
		self._setter_access_tracker["ButtonFlex5"] = {}
		self._ButtonFlex5 = ButtonFlex(new_state)

	@property
	def Anchor14(self):
		self._getter_access_tracker["Anchor14"] = {}
		return self._Anchor14
	@Anchor14.setter
	def Anchor14(self, new_state):
		self._setter_access_tracker["Anchor14"] = {}
		self._Anchor14 = Anchor(new_state)

	@property
	def Flex17(self):
		self._getter_access_tracker["Flex17"] = {}
		return self._Flex17
	@Flex17.setter
	def Flex17(self, new_state):
		self._setter_access_tracker["Flex17"] = {}
		self._Flex17 = Flex(new_state)

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
	def ButtonFlex7(self):
		self._getter_access_tracker["ButtonFlex7"] = {}
		return self._ButtonFlex7
	@ButtonFlex7.setter
	def ButtonFlex7(self, new_state):
		self._setter_access_tracker["ButtonFlex7"] = {}
		self._ButtonFlex7 = ButtonFlex(new_state)

	@property
	def Anchor16(self):
		self._getter_access_tracker["Anchor16"] = {}
		return self._Anchor16
	@Anchor16.setter
	def Anchor16(self, new_state):
		self._setter_access_tracker["Anchor16"] = {}
		self._Anchor16 = Anchor(new_state)

	@property
	def Flex19(self):
		self._getter_access_tracker["Flex19"] = {}
		return self._Flex19
	@Flex19.setter
	def Flex19(self, new_state):
		self._setter_access_tracker["Flex19"] = {}
		self._Flex19 = Flex(new_state)

	@property
	def Flex20(self):
		self._getter_access_tracker["Flex20"] = {}
		return self._Flex20
	@Flex20.setter
	def Flex20(self, new_state):
		self._setter_access_tracker["Flex20"] = {}
		self._Flex20 = Flex(new_state)

	@property
	def FramerFlex3(self):
		self._getter_access_tracker["FramerFlex3"] = {}
		return self._FramerFlex3
	@FramerFlex3.setter
	def FramerFlex3(self, new_state):
		self._setter_access_tracker["FramerFlex3"] = {}
		self._FramerFlex3 = FramerFlex(new_state)

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		self._Image3 = Image(new_state)

	@property
	def Image4(self):
		self._getter_access_tracker["Image4"] = {}
		return self._Image4
	@Image4.setter
	def Image4(self, new_state):
		self._setter_access_tracker["Image4"] = {}
		self._Image4 = Image(new_state)

	@property
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		self._Image5 = Image(new_state)

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		self._Image6 = Image(new_state)

	@property
	def Image7(self):
		self._getter_access_tracker["Image7"] = {}
		return self._Image7
	@Image7.setter
	def Image7(self, new_state):
		self._setter_access_tracker["Image7"] = {}
		self._Image7 = Image(new_state)

	@property
	def Image8(self):
		self._getter_access_tracker["Image8"] = {}
		return self._Image8
	@Image8.setter
	def Image8(self, new_state):
		self._setter_access_tracker["Image8"] = {}
		self._Image8 = Image(new_state)

	@property
	def Flex21(self):
		self._getter_access_tracker["Flex21"] = {}
		return self._Flex21
	@Flex21.setter
	def Flex21(self, new_state):
		self._setter_access_tracker["Flex21"] = {}
		self._Flex21 = Flex(new_state)

	@property
	def Flex22(self):
		self._getter_access_tracker["Flex22"] = {}
		return self._Flex22
	@Flex22.setter
	def Flex22(self, new_state):
		self._setter_access_tracker["Flex22"] = {}
		self._Flex22 = Flex(new_state)

	@property
	def FramerFlex4(self):
		self._getter_access_tracker["FramerFlex4"] = {}
		return self._FramerFlex4
	@FramerFlex4.setter
	def FramerFlex4(self, new_state):
		self._setter_access_tracker["FramerFlex4"] = {}
		self._FramerFlex4 = FramerFlex(new_state)

	@property
	def Flex25(self):
		self._getter_access_tracker["Flex25"] = {}
		return self._Flex25
	@Flex25.setter
	def Flex25(self, new_state):
		self._setter_access_tracker["Flex25"] = {}
		self._Flex25 = Flex(new_state)

	@property
	def Div1(self):
		self._getter_access_tracker["Div1"] = {}
		return self._Div1
	@Div1.setter
	def Div1(self, new_state):
		self._setter_access_tracker["Div1"] = {}
		self._Div1 = Div(new_state)

	@property
	def TextBox30(self):
		self._getter_access_tracker["TextBox30"] = {}
		return self._TextBox30
	@TextBox30.setter
	def TextBox30(self, new_state):
		self._setter_access_tracker["TextBox30"] = {}
		self._TextBox30 = TextBox(new_state)

	@property
	def TextBox31(self):
		self._getter_access_tracker["TextBox31"] = {}
		return self._TextBox31
	@TextBox31.setter
	def TextBox31(self, new_state):
		self._setter_access_tracker["TextBox31"] = {}
		self._TextBox31 = TextBox(new_state)

	@property
	def TextBox32(self):
		self._getter_access_tracker["TextBox32"] = {}
		return self._TextBox32
	@TextBox32.setter
	def TextBox32(self, new_state):
		self._setter_access_tracker["TextBox32"] = {}
		self._TextBox32 = TextBox(new_state)

	@property
	def TextBox33(self):
		self._getter_access_tracker["TextBox33"] = {}
		return self._TextBox33
	@TextBox33.setter
	def TextBox33(self, new_state):
		self._setter_access_tracker["TextBox33"] = {}
		self._TextBox33 = TextBox(new_state)

	@property
	def TextBox34(self):
		self._getter_access_tracker["TextBox34"] = {}
		return self._TextBox34
	@TextBox34.setter
	def TextBox34(self, new_state):
		self._setter_access_tracker["TextBox34"] = {}
		self._TextBox34 = TextBox(new_state)

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
	def Flex26(self):
		self._getter_access_tracker["Flex26"] = {}
		return self._Flex26
	@Flex26.setter
	def Flex26(self, new_state):
		self._setter_access_tracker["Flex26"] = {}
		self._Flex26 = Flex(new_state)

	@property
	def FramerFlex7(self):
		self._getter_access_tracker["FramerFlex7"] = {}
		return self._FramerFlex7
	@FramerFlex7.setter
	def FramerFlex7(self, new_state):
		self._setter_access_tracker["FramerFlex7"] = {}
		self._FramerFlex7 = FramerFlex(new_state)

	@property
	def Flex32(self):
		self._getter_access_tracker["Flex32"] = {}
		return self._Flex32
	@Flex32.setter
	def Flex32(self, new_state):
		self._setter_access_tracker["Flex32"] = {}
		self._Flex32 = Flex(new_state)

	@property
	def Flex33(self):
		self._getter_access_tracker["Flex33"] = {}
		return self._Flex33
	@Flex33.setter
	def Flex33(self, new_state):
		self._setter_access_tracker["Flex33"] = {}
		self._Flex33 = Flex(new_state)

	@property
	def Flex35(self):
		self._getter_access_tracker["Flex35"] = {}
		return self._Flex35
	@Flex35.setter
	def Flex35(self, new_state):
		self._setter_access_tracker["Flex35"] = {}
		self._Flex35 = Flex(new_state)

	@property
	def Image9(self):
		self._getter_access_tracker["Image9"] = {}
		return self._Image9
	@Image9.setter
	def Image9(self, new_state):
		self._setter_access_tracker["Image9"] = {}
		self._Image9 = Image(new_state)

	@property
	def Div3(self):
		self._getter_access_tracker["Div3"] = {}
		return self._Div3
	@Div3.setter
	def Div3(self, new_state):
		self._setter_access_tracker["Div3"] = {}
		self._Div3 = Div(new_state)

	@property
	def Flex36(self):
		self._getter_access_tracker["Flex36"] = {}
		return self._Flex36
	@Flex36.setter
	def Flex36(self, new_state):
		self._setter_access_tracker["Flex36"] = {}
		self._Flex36 = Flex(new_state)

	@property
	def TextBox37(self):
		self._getter_access_tracker["TextBox37"] = {}
		return self._TextBox37
	@TextBox37.setter
	def TextBox37(self, new_state):
		self._setter_access_tracker["TextBox37"] = {}
		self._TextBox37 = TextBox(new_state)

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
	def Div4(self):
		self._getter_access_tracker["Div4"] = {}
		return self._Div4
	@Div4.setter
	def Div4(self, new_state):
		self._setter_access_tracker["Div4"] = {}
		self._Div4 = Div(new_state)

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
	def ButtonFlex12(self):
		self._getter_access_tracker["ButtonFlex12"] = {}
		return self._ButtonFlex12
	@ButtonFlex12.setter
	def ButtonFlex12(self, new_state):
		self._setter_access_tracker["ButtonFlex12"] = {}
		self._ButtonFlex12 = ButtonFlex(new_state)

	@property
	def Image10(self):
		self._getter_access_tracker["Image10"] = {}
		return self._Image10
	@Image10.setter
	def Image10(self, new_state):
		self._setter_access_tracker["Image10"] = {}
		self._Image10 = Image(new_state)

	@property
	def Anchor21(self):
		self._getter_access_tracker["Anchor21"] = {}
		return self._Anchor21
	@Anchor21.setter
	def Anchor21(self, new_state):
		self._setter_access_tracker["Anchor21"] = {}
		self._Anchor21 = Anchor(new_state)

	@property
	def FramerFlex8(self):
		self._getter_access_tracker["FramerFlex8"] = {}
		return self._FramerFlex8
	@FramerFlex8.setter
	def FramerFlex8(self, new_state):
		self._setter_access_tracker["FramerFlex8"] = {}
		self._FramerFlex8 = FramerFlex(new_state)

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
	def Flex39(self):
		self._getter_access_tracker["Flex39"] = {}
		return self._Flex39
	@Flex39.setter
	def Flex39(self, new_state):
		self._setter_access_tracker["Flex39"] = {}
		self._Flex39 = Flex(new_state)

	@property
	def Flex40(self):
		self._getter_access_tracker["Flex40"] = {}
		return self._Flex40
	@Flex40.setter
	def Flex40(self, new_state):
		self._setter_access_tracker["Flex40"] = {}
		self._Flex40 = Flex(new_state)

	@property
	def FramerFlex9(self):
		self._getter_access_tracker["FramerFlex9"] = {}
		return self._FramerFlex9
	@FramerFlex9.setter
	def FramerFlex9(self, new_state):
		self._setter_access_tracker["FramerFlex9"] = {}
		self._FramerFlex9 = FramerFlex(new_state)

	@property
	def Flex41(self):
		self._getter_access_tracker["Flex41"] = {}
		return self._Flex41
	@Flex41.setter
	def Flex41(self, new_state):
		self._setter_access_tracker["Flex41"] = {}
		self._Flex41 = Flex(new_state)

	@property
	def Flex42(self):
		self._getter_access_tracker["Flex42"] = {}
		return self._Flex42
	@Flex42.setter
	def Flex42(self, new_state):
		self._setter_access_tracker["Flex42"] = {}
		self._Flex42 = Flex(new_state)

	@property
	def Flex43(self):
		self._getter_access_tracker["Flex43"] = {}
		return self._Flex43
	@Flex43.setter
	def Flex43(self, new_state):
		self._setter_access_tracker["Flex43"] = {}
		self._Flex43 = Flex(new_state)

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
	def ButtonFlex13(self):
		self._getter_access_tracker["ButtonFlex13"] = {}
		return self._ButtonFlex13
	@ButtonFlex13.setter
	def ButtonFlex13(self, new_state):
		self._setter_access_tracker["ButtonFlex13"] = {}
		self._ButtonFlex13 = ButtonFlex(new_state)

	@property
	def Anchor22(self):
		self._getter_access_tracker["Anchor22"] = {}
		return self._Anchor22
	@Anchor22.setter
	def Anchor22(self, new_state):
		self._setter_access_tracker["Anchor22"] = {}
		self._Anchor22 = Anchor(new_state)

	@property
	def Div5(self):
		self._getter_access_tracker["Div5"] = {}
		return self._Div5
	@Div5.setter
	def Div5(self, new_state):
		self._setter_access_tracker["Div5"] = {}
		self._Div5 = Div(new_state)

	@property
	def TextBox44(self):
		self._getter_access_tracker["TextBox44"] = {}
		return self._TextBox44
	@TextBox44.setter
	def TextBox44(self, new_state):
		self._setter_access_tracker["TextBox44"] = {}
		self._TextBox44 = TextBox(new_state)

	@property
	def Flex44(self):
		self._getter_access_tracker["Flex44"] = {}
		return self._Flex44
	@Flex44.setter
	def Flex44(self, new_state):
		self._setter_access_tracker["Flex44"] = {}
		self._Flex44 = Flex(new_state)

	@property
	def Flex45(self):
		self._getter_access_tracker["Flex45"] = {}
		return self._Flex45
	@Flex45.setter
	def Flex45(self, new_state):
		self._setter_access_tracker["Flex45"] = {}
		self._Flex45 = Flex(new_state)

	@property
	def TextBox45(self):
		self._getter_access_tracker["TextBox45"] = {}
		return self._TextBox45
	@TextBox45.setter
	def TextBox45(self, new_state):
		self._setter_access_tracker["TextBox45"] = {}
		self._TextBox45 = TextBox(new_state)

	@property
	def TextBox46(self):
		self._getter_access_tracker["TextBox46"] = {}
		return self._TextBox46
	@TextBox46.setter
	def TextBox46(self, new_state):
		self._setter_access_tracker["TextBox46"] = {}
		self._TextBox46 = TextBox(new_state)

	@property
	def Div6(self):
		self._getter_access_tracker["Div6"] = {}
		return self._Div6
	@Div6.setter
	def Div6(self, new_state):
		self._setter_access_tracker["Div6"] = {}
		self._Div6 = Div(new_state)

	@property
	def Div7(self):
		self._getter_access_tracker["Div7"] = {}
		return self._Div7
	@Div7.setter
	def Div7(self, new_state):
		self._setter_access_tracker["Div7"] = {}
		self._Div7 = Div(new_state)

	@property
	def Image11(self):
		self._getter_access_tracker["Image11"] = {}
		return self._Image11
	@Image11.setter
	def Image11(self, new_state):
		self._setter_access_tracker["Image11"] = {}
		self._Image11 = Image(new_state)

	@property
	def Image12(self):
		self._getter_access_tracker["Image12"] = {}
		return self._Image12
	@Image12.setter
	def Image12(self, new_state):
		self._setter_access_tracker["Image12"] = {}
		self._Image12 = Image(new_state)

	@property
	def Image13(self):
		self._getter_access_tracker["Image13"] = {}
		return self._Image13
	@Image13.setter
	def Image13(self, new_state):
		self._setter_access_tracker["Image13"] = {}
		self._Image13 = Image(new_state)

	@property
	def Flex46(self):
		self._getter_access_tracker["Flex46"] = {}
		return self._Flex46
	@Flex46.setter
	def Flex46(self, new_state):
		self._setter_access_tracker["Flex46"] = {}
		self._Flex46 = Flex(new_state)

	@property
	def Flex47(self):
		self._getter_access_tracker["Flex47"] = {}
		return self._Flex47
	@Flex47.setter
	def Flex47(self, new_state):
		self._setter_access_tracker["Flex47"] = {}
		self._Flex47 = Flex(new_state)

	@property
	def FramerFlex10(self):
		self._getter_access_tracker["FramerFlex10"] = {}
		return self._FramerFlex10
	@FramerFlex10.setter
	def FramerFlex10(self, new_state):
		self._setter_access_tracker["FramerFlex10"] = {}
		self._FramerFlex10 = FramerFlex(new_state)

	@property
	def Image14(self):
		self._getter_access_tracker["Image14"] = {}
		return self._Image14
	@Image14.setter
	def Image14(self, new_state):
		self._setter_access_tracker["Image14"] = {}
		self._Image14 = Image(new_state)

	@property
	def Flex50(self):
		self._getter_access_tracker["Flex50"] = {}
		return self._Flex50
	@Flex50.setter
	def Flex50(self, new_state):
		self._setter_access_tracker["Flex50"] = {}
		self._Flex50 = Flex(new_state)

	@property
	def Flex51(self):
		self._getter_access_tracker["Flex51"] = {}
		return self._Flex51
	@Flex51.setter
	def Flex51(self, new_state):
		self._setter_access_tracker["Flex51"] = {}
		self._Flex51 = Flex(new_state)

	@property
	def Div8(self):
		self._getter_access_tracker["Div8"] = {}
		return self._Div8
	@Div8.setter
	def Div8(self, new_state):
		self._setter_access_tracker["Div8"] = {}
		self._Div8 = Div(new_state)

	@property
	def TextBox47(self):
		self._getter_access_tracker["TextBox47"] = {}
		return self._TextBox47
	@TextBox47.setter
	def TextBox47(self, new_state):
		self._setter_access_tracker["TextBox47"] = {}
		self._TextBox47 = TextBox(new_state)

	@property
	def Flex52(self):
		self._getter_access_tracker["Flex52"] = {}
		return self._Flex52
	@Flex52.setter
	def Flex52(self, new_state):
		self._setter_access_tracker["Flex52"] = {}
		self._Flex52 = Flex(new_state)

	@property
	def Flex53(self):
		self._getter_access_tracker["Flex53"] = {}
		return self._Flex53
	@Flex53.setter
	def Flex53(self, new_state):
		self._setter_access_tracker["Flex53"] = {}
		self._Flex53 = Flex(new_state)

	@property
	def Flex54(self):
		self._getter_access_tracker["Flex54"] = {}
		return self._Flex54
	@Flex54.setter
	def Flex54(self, new_state):
		self._setter_access_tracker["Flex54"] = {}
		self._Flex54 = Flex(new_state)

	@property
	def TextBox48(self):
		self._getter_access_tracker["TextBox48"] = {}
		return self._TextBox48
	@TextBox48.setter
	def TextBox48(self, new_state):
		self._setter_access_tracker["TextBox48"] = {}
		self._TextBox48 = TextBox(new_state)

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
	def TextBox51(self):
		self._getter_access_tracker["TextBox51"] = {}
		return self._TextBox51
	@TextBox51.setter
	def TextBox51(self, new_state):
		self._setter_access_tracker["TextBox51"] = {}
		self._TextBox51 = TextBox(new_state)

	@property
	def Flex55(self):
		self._getter_access_tracker["Flex55"] = {}
		return self._Flex55
	@Flex55.setter
	def Flex55(self, new_state):
		self._setter_access_tracker["Flex55"] = {}
		self._Flex55 = Flex(new_state)

	@property
	def TextBox52(self):
		self._getter_access_tracker["TextBox52"] = {}
		return self._TextBox52
	@TextBox52.setter
	def TextBox52(self, new_state):
		self._setter_access_tracker["TextBox52"] = {}
		self._TextBox52 = TextBox(new_state)

	@property
	def TextBox53(self):
		self._getter_access_tracker["TextBox53"] = {}
		return self._TextBox53
	@TextBox53.setter
	def TextBox53(self, new_state):
		self._setter_access_tracker["TextBox53"] = {}
		self._TextBox53 = TextBox(new_state)

	@property
	def Flex56(self):
		self._getter_access_tracker["Flex56"] = {}
		return self._Flex56
	@Flex56.setter
	def Flex56(self, new_state):
		self._setter_access_tracker["Flex56"] = {}
		self._Flex56 = Flex(new_state)

	@property
	def TextBox54(self):
		self._getter_access_tracker["TextBox54"] = {}
		return self._TextBox54
	@TextBox54.setter
	def TextBox54(self, new_state):
		self._setter_access_tracker["TextBox54"] = {}
		self._TextBox54 = TextBox(new_state)

	@property
	def TextBox55(self):
		self._getter_access_tracker["TextBox55"] = {}
		return self._TextBox55
	@TextBox55.setter
	def TextBox55(self, new_state):
		self._setter_access_tracker["TextBox55"] = {}
		self._TextBox55 = TextBox(new_state)

	@property
	def Flex57(self):
		self._getter_access_tracker["Flex57"] = {}
		return self._Flex57
	@Flex57.setter
	def Flex57(self, new_state):
		self._setter_access_tracker["Flex57"] = {}
		self._Flex57 = Flex(new_state)

	@property
	def Flex58(self):
		self._getter_access_tracker["Flex58"] = {}
		return self._Flex58
	@Flex58.setter
	def Flex58(self, new_state):
		self._setter_access_tracker["Flex58"] = {}
		self._Flex58 = Flex(new_state)

	@property
	def Flex59(self):
		self._getter_access_tracker["Flex59"] = {}
		return self._Flex59
	@Flex59.setter
	def Flex59(self, new_state):
		self._setter_access_tracker["Flex59"] = {}
		self._Flex59 = Flex(new_state)

	@property
	def FramerFlex11(self):
		self._getter_access_tracker["FramerFlex11"] = {}
		return self._FramerFlex11
	@FramerFlex11.setter
	def FramerFlex11(self, new_state):
		self._setter_access_tracker["FramerFlex11"] = {}
		self._FramerFlex11 = FramerFlex(new_state)

	@property
	def FramerFlex12(self):
		self._getter_access_tracker["FramerFlex12"] = {}
		return self._FramerFlex12
	@FramerFlex12.setter
	def FramerFlex12(self, new_state):
		self._setter_access_tracker["FramerFlex12"] = {}
		self._FramerFlex12 = FramerFlex(new_state)

	@property
	def Div9(self):
		self._getter_access_tracker["Div9"] = {}
		return self._Div9
	@Div9.setter
	def Div9(self, new_state):
		self._setter_access_tracker["Div9"] = {}
		self._Div9 = Div(new_state)

	@property
	def TextBox56(self):
		self._getter_access_tracker["TextBox56"] = {}
		return self._TextBox56
	@TextBox56.setter
	def TextBox56(self, new_state):
		self._setter_access_tracker["TextBox56"] = {}
		self._TextBox56 = TextBox(new_state)

	@property
	def Flex60(self):
		self._getter_access_tracker["Flex60"] = {}
		return self._Flex60
	@Flex60.setter
	def Flex60(self, new_state):
		self._setter_access_tracker["Flex60"] = {}
		self._Flex60 = Flex(new_state)

	@property
	def Flex61(self):
		self._getter_access_tracker["Flex61"] = {}
		return self._Flex61
	@Flex61.setter
	def Flex61(self, new_state):
		self._setter_access_tracker["Flex61"] = {}
		self._Flex61 = Flex(new_state)

	@property
	def Flex62(self):
		self._getter_access_tracker["Flex62"] = {}
		return self._Flex62
	@Flex62.setter
	def Flex62(self, new_state):
		self._setter_access_tracker["Flex62"] = {}
		self._Flex62 = Flex(new_state)

	@property
	def Flex63(self):
		self._getter_access_tracker["Flex63"] = {}
		return self._Flex63
	@Flex63.setter
	def Flex63(self, new_state):
		self._setter_access_tracker["Flex63"] = {}
		self._Flex63 = Flex(new_state)

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
	def Flex64(self):
		self._getter_access_tracker["Flex64"] = {}
		return self._Flex64
	@Flex64.setter
	def Flex64(self, new_state):
		self._setter_access_tracker["Flex64"] = {}
		self._Flex64 = Flex(new_state)

	@property
	def Flex65(self):
		self._getter_access_tracker["Flex65"] = {}
		return self._Flex65
	@Flex65.setter
	def Flex65(self, new_state):
		self._setter_access_tracker["Flex65"] = {}
		self._Flex65 = Flex(new_state)

	@property
	def Flex66(self):
		self._getter_access_tracker["Flex66"] = {}
		return self._Flex66
	@Flex66.setter
	def Flex66(self, new_state):
		self._setter_access_tracker["Flex66"] = {}
		self._Flex66 = Flex(new_state)

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
	def Flex67(self):
		self._getter_access_tracker["Flex67"] = {}
		return self._Flex67
	@Flex67.setter
	def Flex67(self, new_state):
		self._setter_access_tracker["Flex67"] = {}
		self._Flex67 = Flex(new_state)

	@property
	def Flex68(self):
		self._getter_access_tracker["Flex68"] = {}
		return self._Flex68
	@Flex68.setter
	def Flex68(self, new_state):
		self._setter_access_tracker["Flex68"] = {}
		self._Flex68 = Flex(new_state)

	@property
	def Flex69(self):
		self._getter_access_tracker["Flex69"] = {}
		return self._Flex69
	@Flex69.setter
	def Flex69(self, new_state):
		self._setter_access_tracker["Flex69"] = {}
		self._Flex69 = Flex(new_state)

	@property
	def Image15(self):
		self._getter_access_tracker["Image15"] = {}
		return self._Image15
	@Image15.setter
	def Image15(self, new_state):
		self._setter_access_tracker["Image15"] = {}
		self._Image15 = Image(new_state)

	@property
	def Flex70(self):
		self._getter_access_tracker["Flex70"] = {}
		return self._Flex70
	@Flex70.setter
	def Flex70(self, new_state):
		self._setter_access_tracker["Flex70"] = {}
		self._Flex70 = Flex(new_state)

	@property
	def ScaleFlex4(self):
		self._getter_access_tracker["ScaleFlex4"] = {}
		return self._ScaleFlex4
	@ScaleFlex4.setter
	def ScaleFlex4(self, new_state):
		self._setter_access_tracker["ScaleFlex4"] = {}
		self._ScaleFlex4 = ScaleFlex(new_state)

	@property
	def Image16(self):
		self._getter_access_tracker["Image16"] = {}
		return self._Image16
	@Image16.setter
	def Image16(self, new_state):
		self._setter_access_tracker["Image16"] = {}
		self._Image16 = Image(new_state)

	@property
	def Anchor23(self):
		self._getter_access_tracker["Anchor23"] = {}
		return self._Anchor23
	@Anchor23.setter
	def Anchor23(self, new_state):
		self._setter_access_tracker["Anchor23"] = {}
		self._Anchor23 = Anchor(new_state)

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
	def ButtonFlex14(self):
		self._getter_access_tracker["ButtonFlex14"] = {}
		return self._ButtonFlex14
	@ButtonFlex14.setter
	def ButtonFlex14(self, new_state):
		self._setter_access_tracker["ButtonFlex14"] = {}
		self._ButtonFlex14 = ButtonFlex(new_state)

	@property
	def ButtonFlex15(self):
		self._getter_access_tracker["ButtonFlex15"] = {}
		return self._ButtonFlex15
	@ButtonFlex15.setter
	def ButtonFlex15(self, new_state):
		self._setter_access_tracker["ButtonFlex15"] = {}
		self._ButtonFlex15 = ButtonFlex(new_state)

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
	def Flex73(self):
		self._getter_access_tracker["Flex73"] = {}
		return self._Flex73
	@Flex73.setter
	def Flex73(self, new_state):
		self._setter_access_tracker["Flex73"] = {}
		self._Flex73 = Flex(new_state)

	@property
	def Flex74(self):
		self._getter_access_tracker["Flex74"] = {}
		return self._Flex74
	@Flex74.setter
	def Flex74(self, new_state):
		self._setter_access_tracker["Flex74"] = {}
		self._Flex74 = Flex(new_state)

	@property
	def FramerFlex13(self):
		self._getter_access_tracker["FramerFlex13"] = {}
		return self._FramerFlex13
	@FramerFlex13.setter
	def FramerFlex13(self, new_state):
		self._setter_access_tracker["FramerFlex13"] = {}
		self._FramerFlex13 = FramerFlex(new_state)

	@property
	def FramerFlex14(self):
		self._getter_access_tracker["FramerFlex14"] = {}
		return self._FramerFlex14
	@FramerFlex14.setter
	def FramerFlex14(self, new_state):
		self._setter_access_tracker["FramerFlex14"] = {}
		self._FramerFlex14 = FramerFlex(new_state)

	@property
	def Flex75(self):
		self._getter_access_tracker["Flex75"] = {}
		return self._Flex75
	@Flex75.setter
	def Flex75(self, new_state):
		self._setter_access_tracker["Flex75"] = {}
		self._Flex75 = Flex(new_state)

	@property
	def TextBox73(self):
		self._getter_access_tracker["TextBox73"] = {}
		return self._TextBox73
	@TextBox73.setter
	def TextBox73(self, new_state):
		self._setter_access_tracker["TextBox73"] = {}
		self._TextBox73 = TextBox(new_state)

	@property
	def TextBox74(self):
		self._getter_access_tracker["TextBox74"] = {}
		return self._TextBox74
	@TextBox74.setter
	def TextBox74(self, new_state):
		self._setter_access_tracker["TextBox74"] = {}
		self._TextBox74 = TextBox(new_state)

	@property
	def ButtonFlex16(self):
		self._getter_access_tracker["ButtonFlex16"] = {}
		return self._ButtonFlex16
	@ButtonFlex16.setter
	def ButtonFlex16(self, new_state):
		self._setter_access_tracker["ButtonFlex16"] = {}
		self._ButtonFlex16 = ButtonFlex(new_state)

	@property
	def Anchor26(self):
		self._getter_access_tracker["Anchor26"] = {}
		return self._Anchor26
	@Anchor26.setter
	def Anchor26(self, new_state):
		self._setter_access_tracker["Anchor26"] = {}
		self._Anchor26 = Anchor(new_state)

	@property
	def Div11(self):
		self._getter_access_tracker["Div11"] = {}
		return self._Div11
	@Div11.setter
	def Div11(self, new_state):
		self._setter_access_tracker["Div11"] = {}
		self._Div11 = Div(new_state)

	@property
	def TextBox75(self):
		self._getter_access_tracker["TextBox75"] = {}
		return self._TextBox75
	@TextBox75.setter
	def TextBox75(self, new_state):
		self._setter_access_tracker["TextBox75"] = {}
		self._TextBox75 = TextBox(new_state)

	@property
	def Flex76(self):
		self._getter_access_tracker["Flex76"] = {}
		return self._Flex76
	@Flex76.setter
	def Flex76(self, new_state):
		self._setter_access_tracker["Flex76"] = {}
		self._Flex76 = Flex(new_state)

	@property
	def Flex78(self):
		self._getter_access_tracker["Flex78"] = {}
		return self._Flex78
	@Flex78.setter
	def Flex78(self, new_state):
		self._setter_access_tracker["Flex78"] = {}
		self._Flex78 = Flex(new_state)

	@property
	def TextBox76(self):
		self._getter_access_tracker["TextBox76"] = {}
		return self._TextBox76
	@TextBox76.setter
	def TextBox76(self, new_state):
		self._setter_access_tracker["TextBox76"] = {}
		self._TextBox76 = TextBox(new_state)

	@property
	def Accordion2(self):
		self._getter_access_tracker["Accordion2"] = {}
		return self._Accordion2
	@Accordion2.setter
	def Accordion2(self, new_state):
		self._setter_access_tracker["Accordion2"] = {}
		self._Accordion2 = Accordion(new_state)

	@property
	def Accordion3(self):
		self._getter_access_tracker["Accordion3"] = {}
		return self._Accordion3
	@Accordion3.setter
	def Accordion3(self, new_state):
		self._setter_access_tracker["Accordion3"] = {}
		self._Accordion3 = Accordion(new_state)

	@property
	def TextBox78(self):
		self._getter_access_tracker["TextBox78"] = {}
		return self._TextBox78
	@TextBox78.setter
	def TextBox78(self, new_state):
		self._setter_access_tracker["TextBox78"] = {}
		self._TextBox78 = TextBox(new_state)

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
	def Accordion4(self):
		self._getter_access_tracker["Accordion4"] = {}
		return self._Accordion4
	@Accordion4.setter
	def Accordion4(self, new_state):
		self._setter_access_tracker["Accordion4"] = {}
		self._Accordion4 = Accordion(new_state)

	@property
	def TextBox79(self):
		self._getter_access_tracker["TextBox79"] = {}
		return self._TextBox79
	@TextBox79.setter
	def TextBox79(self, new_state):
		self._setter_access_tracker["TextBox79"] = {}
		self._TextBox79 = TextBox(new_state)

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
	def Accordion5(self):
		self._getter_access_tracker["Accordion5"] = {}
		return self._Accordion5
	@Accordion5.setter
	def Accordion5(self, new_state):
		self._setter_access_tracker["Accordion5"] = {}
		self._Accordion5 = Accordion(new_state)

	@property
	def TextBox80(self):
		self._getter_access_tracker["TextBox80"] = {}
		return self._TextBox80
	@TextBox80.setter
	def TextBox80(self, new_state):
		self._setter_access_tracker["TextBox80"] = {}
		self._TextBox80 = TextBox(new_state)

	@property
	def Flex83(self):
		self._getter_access_tracker["Flex83"] = {}
		return self._Flex83
	@Flex83.setter
	def Flex83(self, new_state):
		self._setter_access_tracker["Flex83"] = {}
		self._Flex83 = Flex(new_state)

	@property
	def Flex84(self):
		self._getter_access_tracker["Flex84"] = {}
		return self._Flex84
	@Flex84.setter
	def Flex84(self, new_state):
		self._setter_access_tracker["Flex84"] = {}
		self._Flex84 = Flex(new_state)

	@property
	def Flex85(self):
		self._getter_access_tracker["Flex85"] = {}
		return self._Flex85
	@Flex85.setter
	def Flex85(self, new_state):
		self._setter_access_tracker["Flex85"] = {}
		self._Flex85 = Flex(new_state)

	@property
	def Flex86(self):
		self._getter_access_tracker["Flex86"] = {}
		return self._Flex86
	@Flex86.setter
	def Flex86(self, new_state):
		self._setter_access_tracker["Flex86"] = {}
		self._Flex86 = Flex(new_state)

	@property
	def FramerFlex15(self):
		self._getter_access_tracker["FramerFlex15"] = {}
		return self._FramerFlex15
	@FramerFlex15.setter
	def FramerFlex15(self, new_state):
		self._setter_access_tracker["FramerFlex15"] = {}
		self._FramerFlex15 = FramerFlex(new_state)

	@property
	def FramerFlex16(self):
		self._getter_access_tracker["FramerFlex16"] = {}
		return self._FramerFlex16
	@FramerFlex16.setter
	def FramerFlex16(self, new_state):
		self._setter_access_tracker["FramerFlex16"] = {}
		self._FramerFlex16 = FramerFlex(new_state)

	@property
	def Div12(self):
		self._getter_access_tracker["Div12"] = {}
		return self._Div12
	@Div12.setter
	def Div12(self, new_state):
		self._setter_access_tracker["Div12"] = {}
		self._Div12 = Div(new_state)

	@property
	def TextBox81(self):
		self._getter_access_tracker["TextBox81"] = {}
		return self._TextBox81
	@TextBox81.setter
	def TextBox81(self, new_state):
		self._setter_access_tracker["TextBox81"] = {}
		self._TextBox81 = TextBox(new_state)

	@property
	def Image26(self):
		self._getter_access_tracker["Image26"] = {}
		return self._Image26
	@Image26.setter
	def Image26(self, new_state):
		self._setter_access_tracker["Image26"] = {}
		self._Image26 = Image(new_state)

	@property
	def Flex103(self):
		self._getter_access_tracker["Flex103"] = {}
		return self._Flex103
	@Flex103.setter
	def Flex103(self, new_state):
		self._setter_access_tracker["Flex103"] = {}
		self._Flex103 = Flex(new_state)

	@property
	def TextBox94(self):
		self._getter_access_tracker["TextBox94"] = {}
		return self._TextBox94
	@TextBox94.setter
	def TextBox94(self, new_state):
		self._setter_access_tracker["TextBox94"] = {}
		self._TextBox94 = TextBox(new_state)

	@property
	def TextBox95(self):
		self._getter_access_tracker["TextBox95"] = {}
		return self._TextBox95
	@TextBox95.setter
	def TextBox95(self, new_state):
		self._setter_access_tracker["TextBox95"] = {}
		self._TextBox95 = TextBox(new_state)

	@property
	def Flex104(self):
		self._getter_access_tracker["Flex104"] = {}
		return self._Flex104
	@Flex104.setter
	def Flex104(self, new_state):
		self._setter_access_tracker["Flex104"] = {}
		self._Flex104 = Flex(new_state)

	@property
	def TextBox96(self):
		self._getter_access_tracker["TextBox96"] = {}
		return self._TextBox96
	@TextBox96.setter
	def TextBox96(self, new_state):
		self._setter_access_tracker["TextBox96"] = {}
		self._TextBox96 = TextBox(new_state)

	@property
	def Div17(self):
		self._getter_access_tracker["Div17"] = {}
		return self._Div17
	@Div17.setter
	def Div17(self, new_state):
		self._setter_access_tracker["Div17"] = {}
		self._Div17 = Div(new_state)

	@property
	def Image27(self):
		self._getter_access_tracker["Image27"] = {}
		return self._Image27
	@Image27.setter
	def Image27(self, new_state):
		self._setter_access_tracker["Image27"] = {}
		self._Image27 = Image(new_state)

	@property
	def Flex105(self):
		self._getter_access_tracker["Flex105"] = {}
		return self._Flex105
	@Flex105.setter
	def Flex105(self, new_state):
		self._setter_access_tracker["Flex105"] = {}
		self._Flex105 = Flex(new_state)

	@property
	def Flex106(self):
		self._getter_access_tracker["Flex106"] = {}
		return self._Flex106
	@Flex106.setter
	def Flex106(self, new_state):
		self._setter_access_tracker["Flex106"] = {}
		self._Flex106 = Flex(new_state)

	@property
	def ScaleFlex9(self):
		self._getter_access_tracker["ScaleFlex9"] = {}
		return self._ScaleFlex9
	@ScaleFlex9.setter
	def ScaleFlex9(self, new_state):
		self._setter_access_tracker["ScaleFlex9"] = {}
		self._ScaleFlex9 = ScaleFlex(new_state)

	@property
	def Image28(self):
		self._getter_access_tracker["Image28"] = {}
		return self._Image28
	@Image28.setter
	def Image28(self, new_state):
		self._setter_access_tracker["Image28"] = {}
		self._Image28 = Image(new_state)

	@property
	def TextBox97(self):
		self._getter_access_tracker["TextBox97"] = {}
		return self._TextBox97
	@TextBox97.setter
	def TextBox97(self, new_state):
		self._setter_access_tracker["TextBox97"] = {}
		self._TextBox97 = TextBox(new_state)

	@property
	def TextBox98(self):
		self._getter_access_tracker["TextBox98"] = {}
		return self._TextBox98
	@TextBox98.setter
	def TextBox98(self, new_state):
		self._setter_access_tracker["TextBox98"] = {}
		self._TextBox98 = TextBox(new_state)

	@property
	def Flex107(self):
		self._getter_access_tracker["Flex107"] = {}
		return self._Flex107
	@Flex107.setter
	def Flex107(self, new_state):
		self._setter_access_tracker["Flex107"] = {}
		self._Flex107 = Flex(new_state)

	@property
	def Image29(self):
		self._getter_access_tracker["Image29"] = {}
		return self._Image29
	@Image29.setter
	def Image29(self, new_state):
		self._setter_access_tracker["Image29"] = {}
		self._Image29 = Image(new_state)

	@property
	def Div18(self):
		self._getter_access_tracker["Div18"] = {}
		return self._Div18
	@Div18.setter
	def Div18(self, new_state):
		self._setter_access_tracker["Div18"] = {}
		self._Div18 = Div(new_state)

	@property
	def TextBox99(self):
		self._getter_access_tracker["TextBox99"] = {}
		return self._TextBox99
	@TextBox99.setter
	def TextBox99(self, new_state):
		self._setter_access_tracker["TextBox99"] = {}
		self._TextBox99 = TextBox(new_state)

	@property
	def Flex108(self):
		self._getter_access_tracker["Flex108"] = {}
		return self._Flex108
	@Flex108.setter
	def Flex108(self, new_state):
		self._setter_access_tracker["Flex108"] = {}
		self._Flex108 = Flex(new_state)

	@property
	def Flex109(self):
		self._getter_access_tracker["Flex109"] = {}
		return self._Flex109
	@Flex109.setter
	def Flex109(self, new_state):
		self._setter_access_tracker["Flex109"] = {}
		self._Flex109 = Flex(new_state)

	@property
	def Flex110(self):
		self._getter_access_tracker["Flex110"] = {}
		return self._Flex110
	@Flex110.setter
	def Flex110(self, new_state):
		self._setter_access_tracker["Flex110"] = {}
		self._Flex110 = Flex(new_state)

	@property
	def ScaleFlex10(self):
		self._getter_access_tracker["ScaleFlex10"] = {}
		return self._ScaleFlex10
	@ScaleFlex10.setter
	def ScaleFlex10(self, new_state):
		self._setter_access_tracker["ScaleFlex10"] = {}
		self._ScaleFlex10 = ScaleFlex(new_state)

	@property
	def Image30(self):
		self._getter_access_tracker["Image30"] = {}
		return self._Image30
	@Image30.setter
	def Image30(self, new_state):
		self._setter_access_tracker["Image30"] = {}
		self._Image30 = Image(new_state)

	@property
	def TextBox100(self):
		self._getter_access_tracker["TextBox100"] = {}
		return self._TextBox100
	@TextBox100.setter
	def TextBox100(self, new_state):
		self._setter_access_tracker["TextBox100"] = {}
		self._TextBox100 = TextBox(new_state)

	@property
	def TextBox101(self):
		self._getter_access_tracker["TextBox101"] = {}
		return self._TextBox101
	@TextBox101.setter
	def TextBox101(self, new_state):
		self._setter_access_tracker["TextBox101"] = {}
		self._TextBox101 = TextBox(new_state)

	@property
	def Flex111(self):
		self._getter_access_tracker["Flex111"] = {}
		return self._Flex111
	@Flex111.setter
	def Flex111(self, new_state):
		self._setter_access_tracker["Flex111"] = {}
		self._Flex111 = Flex(new_state)

	@property
	def Image31(self):
		self._getter_access_tracker["Image31"] = {}
		return self._Image31
	@Image31.setter
	def Image31(self, new_state):
		self._setter_access_tracker["Image31"] = {}
		self._Image31 = Image(new_state)

	@property
	def Div19(self):
		self._getter_access_tracker["Div19"] = {}
		return self._Div19
	@Div19.setter
	def Div19(self, new_state):
		self._setter_access_tracker["Div19"] = {}
		self._Div19 = Div(new_state)

	@property
	def TextBox102(self):
		self._getter_access_tracker["TextBox102"] = {}
		return self._TextBox102
	@TextBox102.setter
	def TextBox102(self, new_state):
		self._setter_access_tracker["TextBox102"] = {}
		self._TextBox102 = TextBox(new_state)

	@property
	def Flex112(self):
		self._getter_access_tracker["Flex112"] = {}
		return self._Flex112
	@Flex112.setter
	def Flex112(self, new_state):
		self._setter_access_tracker["Flex112"] = {}
		self._Flex112 = Flex(new_state)

	@property
	def Flex113(self):
		self._getter_access_tracker["Flex113"] = {}
		return self._Flex113
	@Flex113.setter
	def Flex113(self, new_state):
		self._setter_access_tracker["Flex113"] = {}
		self._Flex113 = Flex(new_state)

	@property
	def Flex114(self):
		self._getter_access_tracker["Flex114"] = {}
		return self._Flex114
	@Flex114.setter
	def Flex114(self, new_state):
		self._setter_access_tracker["Flex114"] = {}
		self._Flex114 = Flex(new_state)

	@property
	def ScaleFlex11(self):
		self._getter_access_tracker["ScaleFlex11"] = {}
		return self._ScaleFlex11
	@ScaleFlex11.setter
	def ScaleFlex11(self, new_state):
		self._setter_access_tracker["ScaleFlex11"] = {}
		self._ScaleFlex11 = ScaleFlex(new_state)

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
	def Image32(self):
		self._getter_access_tracker["Image32"] = {}
		return self._Image32
	@Image32.setter
	def Image32(self, new_state):
		self._setter_access_tracker["Image32"] = {}
		self._Image32 = Image(new_state)

	@property
	def Flex115(self):
		self._getter_access_tracker["Flex115"] = {}
		return self._Flex115
	@Flex115.setter
	def Flex115(self, new_state):
		self._setter_access_tracker["Flex115"] = {}
		self._Flex115 = Flex(new_state)

	@property
	def TextBox103(self):
		self._getter_access_tracker["TextBox103"] = {}
		return self._TextBox103
	@TextBox103.setter
	def TextBox103(self, new_state):
		self._setter_access_tracker["TextBox103"] = {}
		self._TextBox103 = TextBox(new_state)

	@property
	def TextBox104(self):
		self._getter_access_tracker["TextBox104"] = {}
		return self._TextBox104
	@TextBox104.setter
	def TextBox104(self, new_state):
		self._setter_access_tracker["TextBox104"] = {}
		self._TextBox104 = TextBox(new_state)

	@property
	def Flex116(self):
		self._getter_access_tracker["Flex116"] = {}
		return self._Flex116
	@Flex116.setter
	def Flex116(self, new_state):
		self._setter_access_tracker["Flex116"] = {}
		self._Flex116 = Flex(new_state)

	@property
	def TextBox105(self):
		self._getter_access_tracker["TextBox105"] = {}
		return self._TextBox105
	@TextBox105.setter
	def TextBox105(self, new_state):
		self._setter_access_tracker["TextBox105"] = {}
		self._TextBox105 = TextBox(new_state)

	@property
	def Div20(self):
		self._getter_access_tracker["Div20"] = {}
		return self._Div20
	@Div20.setter
	def Div20(self, new_state):
		self._setter_access_tracker["Div20"] = {}
		self._Div20 = Div(new_state)

	@property
	def Image33(self):
		self._getter_access_tracker["Image33"] = {}
		return self._Image33
	@Image33.setter
	def Image33(self, new_state):
		self._setter_access_tracker["Image33"] = {}
		self._Image33 = Image(new_state)

	@property
	def Flex117(self):
		self._getter_access_tracker["Flex117"] = {}
		return self._Flex117
	@Flex117.setter
	def Flex117(self, new_state):
		self._setter_access_tracker["Flex117"] = {}
		self._Flex117 = Flex(new_state)

	@property
	def Flex118(self):
		self._getter_access_tracker["Flex118"] = {}
		return self._Flex118
	@Flex118.setter
	def Flex118(self, new_state):
		self._setter_access_tracker["Flex118"] = {}
		self._Flex118 = Flex(new_state)

	@property
	def ScaleFlex12(self):
		self._getter_access_tracker["ScaleFlex12"] = {}
		return self._ScaleFlex12
	@ScaleFlex12.setter
	def ScaleFlex12(self, new_state):
		self._setter_access_tracker["ScaleFlex12"] = {}
		self._ScaleFlex12 = ScaleFlex(new_state)

	@property
	def Anchor36(self):
		self._getter_access_tracker["Anchor36"] = {}
		return self._Anchor36
	@Anchor36.setter
	def Anchor36(self, new_state):
		self._setter_access_tracker["Anchor36"] = {}
		self._Anchor36 = Anchor(new_state)

	@property
	def Image34(self):
		self._getter_access_tracker["Image34"] = {}
		return self._Image34
	@Image34.setter
	def Image34(self, new_state):
		self._setter_access_tracker["Image34"] = {}
		self._Image34 = Image(new_state)

	@property
	def Flex119(self):
		self._getter_access_tracker["Flex119"] = {}
		return self._Flex119
	@Flex119.setter
	def Flex119(self, new_state):
		self._setter_access_tracker["Flex119"] = {}
		self._Flex119 = Flex(new_state)

	@property
	def TextBox106(self):
		self._getter_access_tracker["TextBox106"] = {}
		return self._TextBox106
	@TextBox106.setter
	def TextBox106(self, new_state):
		self._setter_access_tracker["TextBox106"] = {}
		self._TextBox106 = TextBox(new_state)

	@property
	def TextBox107(self):
		self._getter_access_tracker["TextBox107"] = {}
		return self._TextBox107
	@TextBox107.setter
	def TextBox107(self, new_state):
		self._setter_access_tracker["TextBox107"] = {}
		self._TextBox107 = TextBox(new_state)

	@property
	def Flex120(self):
		self._getter_access_tracker["Flex120"] = {}
		return self._Flex120
	@Flex120.setter
	def Flex120(self, new_state):
		self._setter_access_tracker["Flex120"] = {}
		self._Flex120 = Flex(new_state)

	@property
	def TextBox108(self):
		self._getter_access_tracker["TextBox108"] = {}
		return self._TextBox108
	@TextBox108.setter
	def TextBox108(self, new_state):
		self._setter_access_tracker["TextBox108"] = {}
		self._TextBox108 = TextBox(new_state)

	@property
	def Div21(self):
		self._getter_access_tracker["Div21"] = {}
		return self._Div21
	@Div21.setter
	def Div21(self, new_state):
		self._setter_access_tracker["Div21"] = {}
		self._Div21 = Div(new_state)

	@property
	def Image35(self):
		self._getter_access_tracker["Image35"] = {}
		return self._Image35
	@Image35.setter
	def Image35(self, new_state):
		self._setter_access_tracker["Image35"] = {}
		self._Image35 = Image(new_state)

	@property
	def Flex121(self):
		self._getter_access_tracker["Flex121"] = {}
		return self._Flex121
	@Flex121.setter
	def Flex121(self, new_state):
		self._setter_access_tracker["Flex121"] = {}
		self._Flex121 = Flex(new_state)

	@property
	def Flex122(self):
		self._getter_access_tracker["Flex122"] = {}
		return self._Flex122
	@Flex122.setter
	def Flex122(self, new_state):
		self._setter_access_tracker["Flex122"] = {}
		self._Flex122 = Flex(new_state)

	@property
	def ScaleFlex13(self):
		self._getter_access_tracker["ScaleFlex13"] = {}
		return self._ScaleFlex13
	@ScaleFlex13.setter
	def ScaleFlex13(self, new_state):
		self._setter_access_tracker["ScaleFlex13"] = {}
		self._ScaleFlex13 = ScaleFlex(new_state)

	@property
	def Anchor37(self):
		self._getter_access_tracker["Anchor37"] = {}
		return self._Anchor37
	@Anchor37.setter
	def Anchor37(self, new_state):
		self._setter_access_tracker["Anchor37"] = {}
		self._Anchor37 = Anchor(new_state)

	@property
	def Image36(self):
		self._getter_access_tracker["Image36"] = {}
		return self._Image36
	@Image36.setter
	def Image36(self, new_state):
		self._setter_access_tracker["Image36"] = {}
		self._Image36 = Image(new_state)

	@property
	def TextBox109(self):
		self._getter_access_tracker["TextBox109"] = {}
		return self._TextBox109
	@TextBox109.setter
	def TextBox109(self, new_state):
		self._setter_access_tracker["TextBox109"] = {}
		self._TextBox109 = TextBox(new_state)

	@property
	def TextBox110(self):
		self._getter_access_tracker["TextBox110"] = {}
		return self._TextBox110
	@TextBox110.setter
	def TextBox110(self, new_state):
		self._setter_access_tracker["TextBox110"] = {}
		self._TextBox110 = TextBox(new_state)

	@property
	def Flex123(self):
		self._getter_access_tracker["Flex123"] = {}
		return self._Flex123
	@Flex123.setter
	def Flex123(self, new_state):
		self._setter_access_tracker["Flex123"] = {}
		self._Flex123 = Flex(new_state)

	@property
	def Image37(self):
		self._getter_access_tracker["Image37"] = {}
		return self._Image37
	@Image37.setter
	def Image37(self, new_state):
		self._setter_access_tracker["Image37"] = {}
		self._Image37 = Image(new_state)

	@property
	def Div22(self):
		self._getter_access_tracker["Div22"] = {}
		return self._Div22
	@Div22.setter
	def Div22(self, new_state):
		self._setter_access_tracker["Div22"] = {}
		self._Div22 = Div(new_state)

	@property
	def TextBox111(self):
		self._getter_access_tracker["TextBox111"] = {}
		return self._TextBox111
	@TextBox111.setter
	def TextBox111(self, new_state):
		self._setter_access_tracker["TextBox111"] = {}
		self._TextBox111 = TextBox(new_state)

	@property
	def Flex124(self):
		self._getter_access_tracker["Flex124"] = {}
		return self._Flex124
	@Flex124.setter
	def Flex124(self, new_state):
		self._setter_access_tracker["Flex124"] = {}
		self._Flex124 = Flex(new_state)

	@property
	def Flex125(self):
		self._getter_access_tracker["Flex125"] = {}
		return self._Flex125
	@Flex125.setter
	def Flex125(self, new_state):
		self._setter_access_tracker["Flex125"] = {}
		self._Flex125 = Flex(new_state)

	@property
	def Flex126(self):
		self._getter_access_tracker["Flex126"] = {}
		return self._Flex126
	@Flex126.setter
	def Flex126(self, new_state):
		self._setter_access_tracker["Flex126"] = {}
		self._Flex126 = Flex(new_state)

	@property
	def ScaleFlex14(self):
		self._getter_access_tracker["ScaleFlex14"] = {}
		return self._ScaleFlex14
	@ScaleFlex14.setter
	def ScaleFlex14(self, new_state):
		self._setter_access_tracker["ScaleFlex14"] = {}
		self._ScaleFlex14 = ScaleFlex(new_state)

	@property
	def Anchor38(self):
		self._getter_access_tracker["Anchor38"] = {}
		return self._Anchor38
	@Anchor38.setter
	def Anchor38(self, new_state):
		self._setter_access_tracker["Anchor38"] = {}
		self._Anchor38 = Anchor(new_state)

	@property
	def Flex127(self):
		self._getter_access_tracker["Flex127"] = {}
		return self._Flex127
	@Flex127.setter
	def Flex127(self, new_state):
		self._setter_access_tracker["Flex127"] = {}
		self._Flex127 = Flex(new_state)

	@property
	def TextBox112(self):
		self._getter_access_tracker["TextBox112"] = {}
		return self._TextBox112
	@TextBox112.setter
	def TextBox112(self, new_state):
		self._setter_access_tracker["TextBox112"] = {}
		self._TextBox112 = TextBox(new_state)

	@property
	def TextBox117(self):
		self._getter_access_tracker["TextBox117"] = {}
		return self._TextBox117
	@TextBox117.setter
	def TextBox117(self, new_state):
		self._setter_access_tracker["TextBox117"] = {}
		self._TextBox117 = TextBox(new_state)

	@property
	def TextBox118(self):
		self._getter_access_tracker["TextBox118"] = {}
		return self._TextBox118
	@TextBox118.setter
	def TextBox118(self, new_state):
		self._setter_access_tracker["TextBox118"] = {}
		self._TextBox118 = TextBox(new_state)

	@property
	def TextBox119(self):
		self._getter_access_tracker["TextBox119"] = {}
		return self._TextBox119
	@TextBox119.setter
	def TextBox119(self, new_state):
		self._setter_access_tracker["TextBox119"] = {}
		self._TextBox119 = TextBox(new_state)

	@property
	def TextBox120(self):
		self._getter_access_tracker["TextBox120"] = {}
		return self._TextBox120
	@TextBox120.setter
	def TextBox120(self, new_state):
		self._setter_access_tracker["TextBox120"] = {}
		self._TextBox120 = TextBox(new_state)

	@property
	def ButtonFlex19(self):
		self._getter_access_tracker["ButtonFlex19"] = {}
		return self._ButtonFlex19
	@ButtonFlex19.setter
	def ButtonFlex19(self, new_state):
		self._setter_access_tracker["ButtonFlex19"] = {}
		self._ButtonFlex19 = ButtonFlex(new_state)

	@property
	def ButtonFlex20(self):
		self._getter_access_tracker["ButtonFlex20"] = {}
		return self._ButtonFlex20
	@ButtonFlex20.setter
	def ButtonFlex20(self, new_state):
		self._setter_access_tracker["ButtonFlex20"] = {}
		self._ButtonFlex20 = ButtonFlex(new_state)

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
	def Flex130(self):
		self._getter_access_tracker["Flex130"] = {}
		return self._Flex130
	@Flex130.setter
	def Flex130(self, new_state):
		self._setter_access_tracker["Flex130"] = {}
		self._Flex130 = Flex(new_state)

	@property
	def Flex131(self):
		self._getter_access_tracker["Flex131"] = {}
		return self._Flex131
	@Flex131.setter
	def Flex131(self, new_state):
		self._setter_access_tracker["Flex131"] = {}
		self._Flex131 = Flex(new_state)

	@property
	def Flex132(self):
		self._getter_access_tracker["Flex132"] = {}
		return self._Flex132
	@Flex132.setter
	def Flex132(self, new_state):
		self._setter_access_tracker["Flex132"] = {}
		self._Flex132 = Flex(new_state)

	@property
	def Flex133(self):
		self._getter_access_tracker["Flex133"] = {}
		return self._Flex133
	@Flex133.setter
	def Flex133(self, new_state):
		self._setter_access_tracker["Flex133"] = {}
		self._Flex133 = Flex(new_state)

	@property
	def FramerFlex17(self):
		self._getter_access_tracker["FramerFlex17"] = {}
		return self._FramerFlex17
	@FramerFlex17.setter
	def FramerFlex17(self, new_state):
		self._setter_access_tracker["FramerFlex17"] = {}
		self._FramerFlex17 = FramerFlex(new_state)

	@property
	def FramerFlex18(self):
		self._getter_access_tracker["FramerFlex18"] = {}
		return self._FramerFlex18
	@FramerFlex18.setter
	def FramerFlex18(self, new_state):
		self._setter_access_tracker["FramerFlex18"] = {}
		self._FramerFlex18 = FramerFlex(new_state)

	@property
	def Div23(self):
		self._getter_access_tracker["Div23"] = {}
		return self._Div23
	@Div23.setter
	def Div23(self, new_state):
		self._setter_access_tracker["Div23"] = {}
		self._Div23 = Div(new_state)

	@property
	def Flex134(self):
		self._getter_access_tracker["Flex134"] = {}
		return self._Flex134
	@Flex134.setter
	def Flex134(self, new_state):
		self._setter_access_tracker["Flex134"] = {}
		self._Flex134 = Flex(new_state)

	@property
	def Flex135(self):
		self._getter_access_tracker["Flex135"] = {}
		return self._Flex135
	@Flex135.setter
	def Flex135(self, new_state):
		self._setter_access_tracker["Flex135"] = {}
		self._Flex135 = Flex(new_state)

	@property
	def Flex136(self):
		self._getter_access_tracker["Flex136"] = {}
		return self._Flex136
	@Flex136.setter
	def Flex136(self, new_state):
		self._setter_access_tracker["Flex136"] = {}
		self._Flex136 = Flex(new_state)

	@property
	def Image38(self):
		self._getter_access_tracker["Image38"] = {}
		return self._Image38
	@Image38.setter
	def Image38(self, new_state):
		self._setter_access_tracker["Image38"] = {}
		self._Image38 = Image(new_state)

	@property
	def TextBox121(self):
		self._getter_access_tracker["TextBox121"] = {}
		return self._TextBox121
	@TextBox121.setter
	def TextBox121(self, new_state):
		self._setter_access_tracker["TextBox121"] = {}
		self._TextBox121 = TextBox(new_state)

	@property
	def Anchor43(self):
		self._getter_access_tracker["Anchor43"] = {}
		return self._Anchor43
	@Anchor43.setter
	def Anchor43(self, new_state):
		self._setter_access_tracker["Anchor43"] = {}
		self._Anchor43 = Anchor(new_state)

	@property
	def ScaleFlex15(self):
		self._getter_access_tracker["ScaleFlex15"] = {}
		return self._ScaleFlex15
	@ScaleFlex15.setter
	def ScaleFlex15(self, new_state):
		self._setter_access_tracker["ScaleFlex15"] = {}
		self._ScaleFlex15 = ScaleFlex(new_state)

	@property
	def Flex137(self):
		self._getter_access_tracker["Flex137"] = {}
		return self._Flex137
	@Flex137.setter
	def Flex137(self, new_state):
		self._setter_access_tracker["Flex137"] = {}
		self._Flex137 = Flex(new_state)

	@property
	def Flex138(self):
		self._getter_access_tracker["Flex138"] = {}
		return self._Flex138
	@Flex138.setter
	def Flex138(self, new_state):
		self._setter_access_tracker["Flex138"] = {}
		self._Flex138 = Flex(new_state)

	@property
	def Flex139(self):
		self._getter_access_tracker["Flex139"] = {}
		return self._Flex139
	@Flex139.setter
	def Flex139(self, new_state):
		self._setter_access_tracker["Flex139"] = {}
		self._Flex139 = Flex(new_state)

	@property
	def TextBox122(self):
		self._getter_access_tracker["TextBox122"] = {}
		return self._TextBox122
	@TextBox122.setter
	def TextBox122(self, new_state):
		self._setter_access_tracker["TextBox122"] = {}
		self._TextBox122 = TextBox(new_state)

	@property
	def Flex140(self):
		self._getter_access_tracker["Flex140"] = {}
		return self._Flex140
	@Flex140.setter
	def Flex140(self, new_state):
		self._setter_access_tracker["Flex140"] = {}
		self._Flex140 = Flex(new_state)

	@property
	def Anchor44(self):
		self._getter_access_tracker["Anchor44"] = {}
		return self._Anchor44
	@Anchor44.setter
	def Anchor44(self, new_state):
		self._setter_access_tracker["Anchor44"] = {}
		self._Anchor44 = Anchor(new_state)

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
	def Anchor45(self):
		self._getter_access_tracker["Anchor45"] = {}
		return self._Anchor45
	@Anchor45.setter
	def Anchor45(self, new_state):
		self._setter_access_tracker["Anchor45"] = {}
		self._Anchor45 = Anchor(new_state)

	@property
	def FramerText10(self):
		self._getter_access_tracker["FramerText10"] = {}
		return self._FramerText10
	@FramerText10.setter
	def FramerText10(self, new_state):
		self._setter_access_tracker["FramerText10"] = {}
		self._FramerText10 = FramerText(new_state)

	@property
	def Anchor46(self):
		self._getter_access_tracker["Anchor46"] = {}
		return self._Anchor46
	@Anchor46.setter
	def Anchor46(self, new_state):
		self._setter_access_tracker["Anchor46"] = {}
		self._Anchor46 = Anchor(new_state)

	@property
	def FramerText11(self):
		self._getter_access_tracker["FramerText11"] = {}
		return self._FramerText11
	@FramerText11.setter
	def FramerText11(self, new_state):
		self._setter_access_tracker["FramerText11"] = {}
		self._FramerText11 = FramerText(new_state)

	@property
	def Anchor47(self):
		self._getter_access_tracker["Anchor47"] = {}
		return self._Anchor47
	@Anchor47.setter
	def Anchor47(self, new_state):
		self._setter_access_tracker["Anchor47"] = {}
		self._Anchor47 = Anchor(new_state)

	@property
	def FramerText12(self):
		self._getter_access_tracker["FramerText12"] = {}
		return self._FramerText12
	@FramerText12.setter
	def FramerText12(self, new_state):
		self._setter_access_tracker["FramerText12"] = {}
		self._FramerText12 = FramerText(new_state)

	@property
	def Anchor48(self):
		self._getter_access_tracker["Anchor48"] = {}
		return self._Anchor48
	@Anchor48.setter
	def Anchor48(self, new_state):
		self._setter_access_tracker["Anchor48"] = {}
		self._Anchor48 = Anchor(new_state)

	@property
	def FramerText13(self):
		self._getter_access_tracker["FramerText13"] = {}
		return self._FramerText13
	@FramerText13.setter
	def FramerText13(self, new_state):
		self._setter_access_tracker["FramerText13"] = {}
		self._FramerText13 = FramerText(new_state)

	@property
	def Anchor49(self):
		self._getter_access_tracker["Anchor49"] = {}
		return self._Anchor49
	@Anchor49.setter
	def Anchor49(self, new_state):
		self._setter_access_tracker["Anchor49"] = {}
		self._Anchor49 = Anchor(new_state)

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
	def Flex141(self):
		self._getter_access_tracker["Flex141"] = {}
		return self._Flex141
	@Flex141.setter
	def Flex141(self, new_state):
		self._setter_access_tracker["Flex141"] = {}
		self._Flex141 = Flex(new_state)

	@property
	def TextBox123(self):
		self._getter_access_tracker["TextBox123"] = {}
		return self._TextBox123
	@TextBox123.setter
	def TextBox123(self, new_state):
		self._setter_access_tracker["TextBox123"] = {}
		self._TextBox123 = TextBox(new_state)

	@property
	def Flex142(self):
		self._getter_access_tracker["Flex142"] = {}
		return self._Flex142
	@Flex142.setter
	def Flex142(self, new_state):
		self._setter_access_tracker["Flex142"] = {}
		self._Flex142 = Flex(new_state)

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
	def Anchor56(self):
		self._getter_access_tracker["Anchor56"] = {}
		return self._Anchor56
	@Anchor56.setter
	def Anchor56(self, new_state):
		self._setter_access_tracker["Anchor56"] = {}
		self._Anchor56 = Anchor(new_state)

	@property
	def Anchor57(self):
		self._getter_access_tracker["Anchor57"] = {}
		return self._Anchor57
	@Anchor57.setter
	def Anchor57(self, new_state):
		self._setter_access_tracker["Anchor57"] = {}
		self._Anchor57 = Anchor(new_state)

	@property
	def Anchor58(self):
		self._getter_access_tracker["Anchor58"] = {}
		return self._Anchor58
	@Anchor58.setter
	def Anchor58(self, new_state):
		self._setter_access_tracker["Anchor58"] = {}
		self._Anchor58 = Anchor(new_state)

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
	def Flex143(self):
		self._getter_access_tracker["Flex143"] = {}
		return self._Flex143
	@Flex143.setter
	def Flex143(self, new_state):
		self._setter_access_tracker["Flex143"] = {}
		self._Flex143 = Flex(new_state)

	@property
	def TextBox124(self):
		self._getter_access_tracker["TextBox124"] = {}
		return self._TextBox124
	@TextBox124.setter
	def TextBox124(self, new_state):
		self._setter_access_tracker["TextBox124"] = {}
		self._TextBox124 = TextBox(new_state)

	@property
	def Flex144(self):
		self._getter_access_tracker["Flex144"] = {}
		return self._Flex144
	@Flex144.setter
	def Flex144(self, new_state):
		self._setter_access_tracker["Flex144"] = {}
		self._Flex144 = Flex(new_state)

	@property
	def Flex145(self):
		self._getter_access_tracker["Flex145"] = {}
		return self._Flex145
	@Flex145.setter
	def Flex145(self, new_state):
		self._setter_access_tracker["Flex145"] = {}
		self._Flex145 = Flex(new_state)

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
	def FramerText31(self):
		self._getter_access_tracker["FramerText31"] = {}
		return self._FramerText31
	@FramerText31.setter
	def FramerText31(self, new_state):
		self._setter_access_tracker["FramerText31"] = {}
		self._FramerText31 = FramerText(new_state)

	@property
	def Anchor62(self):
		self._getter_access_tracker["Anchor62"] = {}
		return self._Anchor62
	@Anchor62.setter
	def Anchor62(self, new_state):
		self._setter_access_tracker["Anchor62"] = {}
		self._Anchor62 = Anchor(new_state)

	@property
	def Anchor63(self):
		self._getter_access_tracker["Anchor63"] = {}
		return self._Anchor63
	@Anchor63.setter
	def Anchor63(self, new_state):
		self._setter_access_tracker["Anchor63"] = {}
		self._Anchor63 = Anchor(new_state)

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
	def Flex146(self):
		self._getter_access_tracker["Flex146"] = {}
		return self._Flex146
	@Flex146.setter
	def Flex146(self, new_state):
		self._setter_access_tracker["Flex146"] = {}
		self._Flex146 = Flex(new_state)

	@property
	def FramerText32(self):
		self._getter_access_tracker["FramerText32"] = {}
		return self._FramerText32
	@FramerText32.setter
	def FramerText32(self, new_state):
		self._setter_access_tracker["FramerText32"] = {}
		self._FramerText32 = FramerText(new_state)

	@property
	def Anchor68(self):
		self._getter_access_tracker["Anchor68"] = {}
		return self._Anchor68
	@Anchor68.setter
	def Anchor68(self, new_state):
		self._setter_access_tracker["Anchor68"] = {}
		self._Anchor68 = Anchor(new_state)

	@property
	def FramerText33(self):
		self._getter_access_tracker["FramerText33"] = {}
		return self._FramerText33
	@FramerText33.setter
	def FramerText33(self, new_state):
		self._setter_access_tracker["FramerText33"] = {}
		self._FramerText33 = FramerText(new_state)

	@property
	def Anchor69(self):
		self._getter_access_tracker["Anchor69"] = {}
		return self._Anchor69
	@Anchor69.setter
	def Anchor69(self, new_state):
		self._setter_access_tracker["Anchor69"] = {}
		self._Anchor69 = Anchor(new_state)

	@property
	def FramerText34(self):
		self._getter_access_tracker["FramerText34"] = {}
		return self._FramerText34
	@FramerText34.setter
	def FramerText34(self, new_state):
		self._setter_access_tracker["FramerText34"] = {}
		self._FramerText34 = FramerText(new_state)

	@property
	def Anchor70(self):
		self._getter_access_tracker["Anchor70"] = {}
		return self._Anchor70
	@Anchor70.setter
	def Anchor70(self, new_state):
		self._setter_access_tracker["Anchor70"] = {}
		self._Anchor70 = Anchor(new_state)

	@property
	def FramerText35(self):
		self._getter_access_tracker["FramerText35"] = {}
		return self._FramerText35
	@FramerText35.setter
	def FramerText35(self, new_state):
		self._setter_access_tracker["FramerText35"] = {}
		self._FramerText35 = FramerText(new_state)

	@property
	def Anchor71(self):
		self._getter_access_tracker["Anchor71"] = {}
		return self._Anchor71
	@Anchor71.setter
	def Anchor71(self, new_state):
		self._setter_access_tracker["Anchor71"] = {}
		self._Anchor71 = Anchor(new_state)

	@property
	def FramerText36(self):
		self._getter_access_tracker["FramerText36"] = {}
		return self._FramerText36
	@FramerText36.setter
	def FramerText36(self, new_state):
		self._setter_access_tracker["FramerText36"] = {}
		self._FramerText36 = FramerText(new_state)

	@property
	def Anchor72(self):
		self._getter_access_tracker["Anchor72"] = {}
		return self._Anchor72
	@Anchor72.setter
	def Anchor72(self, new_state):
		self._setter_access_tracker["Anchor72"] = {}
		self._Anchor72 = Anchor(new_state)

	@property
	def FramerText37(self):
		self._getter_access_tracker["FramerText37"] = {}
		return self._FramerText37
	@FramerText37.setter
	def FramerText37(self, new_state):
		self._setter_access_tracker["FramerText37"] = {}
		self._FramerText37 = FramerText(new_state)

	@property
	def Anchor73(self):
		self._getter_access_tracker["Anchor73"] = {}
		return self._Anchor73
	@Anchor73.setter
	def Anchor73(self, new_state):
		self._setter_access_tracker["Anchor73"] = {}
		self._Anchor73 = Anchor(new_state)

	@property
	def FramerText38(self):
		self._getter_access_tracker["FramerText38"] = {}
		return self._FramerText38
	@FramerText38.setter
	def FramerText38(self, new_state):
		self._setter_access_tracker["FramerText38"] = {}
		self._FramerText38 = FramerText(new_state)

	@property
	def Anchor74(self):
		self._getter_access_tracker["Anchor74"] = {}
		return self._Anchor74
	@Anchor74.setter
	def Anchor74(self, new_state):
		self._setter_access_tracker["Anchor74"] = {}
		self._Anchor74 = Anchor(new_state)

	@property
	def FramerText39(self):
		self._getter_access_tracker["FramerText39"] = {}
		return self._FramerText39
	@FramerText39.setter
	def FramerText39(self, new_state):
		self._setter_access_tracker["FramerText39"] = {}
		self._FramerText39 = FramerText(new_state)

	@property
	def Anchor75(self):
		self._getter_access_tracker["Anchor75"] = {}
		return self._Anchor75
	@Anchor75.setter
	def Anchor75(self, new_state):
		self._setter_access_tracker["Anchor75"] = {}
		self._Anchor75 = Anchor(new_state)

	@property
	def FramerText40(self):
		self._getter_access_tracker["FramerText40"] = {}
		return self._FramerText40
	@FramerText40.setter
	def FramerText40(self, new_state):
		self._setter_access_tracker["FramerText40"] = {}
		self._FramerText40 = FramerText(new_state)

	@property
	def Anchor76(self):
		self._getter_access_tracker["Anchor76"] = {}
		return self._Anchor76
	@Anchor76.setter
	def Anchor76(self, new_state):
		self._setter_access_tracker["Anchor76"] = {}
		self._Anchor76 = Anchor(new_state)

	@property
	def FramerText41(self):
		self._getter_access_tracker["FramerText41"] = {}
		return self._FramerText41
	@FramerText41.setter
	def FramerText41(self, new_state):
		self._setter_access_tracker["FramerText41"] = {}
		self._FramerText41 = FramerText(new_state)

	@property
	def Anchor77(self):
		self._getter_access_tracker["Anchor77"] = {}
		return self._Anchor77
	@Anchor77.setter
	def Anchor77(self, new_state):
		self._setter_access_tracker["Anchor77"] = {}
		self._Anchor77 = Anchor(new_state)

	@property
	def FramerText42(self):
		self._getter_access_tracker["FramerText42"] = {}
		return self._FramerText42
	@FramerText42.setter
	def FramerText42(self, new_state):
		self._setter_access_tracker["FramerText42"] = {}
		self._FramerText42 = FramerText(new_state)

	@property
	def Anchor78(self):
		self._getter_access_tracker["Anchor78"] = {}
		return self._Anchor78
	@Anchor78.setter
	def Anchor78(self, new_state):
		self._setter_access_tracker["Anchor78"] = {}
		self._Anchor78 = Anchor(new_state)

	@property
	def Flex147(self):
		self._getter_access_tracker["Flex147"] = {}
		return self._Flex147
	@Flex147.setter
	def Flex147(self, new_state):
		self._setter_access_tracker["Flex147"] = {}
		self._Flex147 = Flex(new_state)

	@property
	def TextBox125(self):
		self._getter_access_tracker["TextBox125"] = {}
		return self._TextBox125
	@TextBox125.setter
	def TextBox125(self, new_state):
		self._setter_access_tracker["TextBox125"] = {}
		self._TextBox125 = TextBox(new_state)

	@property
	def ButtonFlex21(self):
		self._getter_access_tracker["ButtonFlex21"] = {}
		return self._ButtonFlex21
	@ButtonFlex21.setter
	def ButtonFlex21(self, new_state):
		self._setter_access_tracker["ButtonFlex21"] = {}
		self._ButtonFlex21 = ButtonFlex(new_state)

	@property
	def Flex148(self):
		self._getter_access_tracker["Flex148"] = {}
		return self._Flex148
	@Flex148.setter
	def Flex148(self, new_state):
		self._setter_access_tracker["Flex148"] = {}
		self._Flex148 = Flex(new_state)

	@property
	def Anchor79(self):
		self._getter_access_tracker["Anchor79"] = {}
		return self._Anchor79
	@Anchor79.setter
	def Anchor79(self, new_state):
		self._setter_access_tracker["Anchor79"] = {}
		self._Anchor79 = Anchor(new_state)

	@property
	def Image39(self):
		self._getter_access_tracker["Image39"] = {}
		return self._Image39
	@Image39.setter
	def Image39(self, new_state):
		self._setter_access_tracker["Image39"] = {}
		self._Image39 = Image(new_state)

	@property
	def Image40(self):
		self._getter_access_tracker["Image40"] = {}
		return self._Image40
	@Image40.setter
	def Image40(self, new_state):
		self._setter_access_tracker["Image40"] = {}
		self._Image40 = Image(new_state)

	@property
	def ButtonFlex22(self):
		self._getter_access_tracker["ButtonFlex22"] = {}
		return self._ButtonFlex22
	@ButtonFlex22.setter
	def ButtonFlex22(self, new_state):
		self._setter_access_tracker["ButtonFlex22"] = {}
		self._ButtonFlex22 = ButtonFlex(new_state)

	@property
	def Anchor80(self):
		self._getter_access_tracker["Anchor80"] = {}
		return self._Anchor80
	@Anchor80.setter
	def Anchor80(self, new_state):
		self._setter_access_tracker["Anchor80"] = {}
		self._Anchor80 = Anchor(new_state)

	@property
	def Image41(self):
		self._getter_access_tracker["Image41"] = {}
		return self._Image41
	@Image41.setter
	def Image41(self, new_state):
		self._setter_access_tracker["Image41"] = {}
		self._Image41 = Image(new_state)

	@property
	def ButtonFlex23(self):
		self._getter_access_tracker["ButtonFlex23"] = {}
		return self._ButtonFlex23
	@ButtonFlex23.setter
	def ButtonFlex23(self, new_state):
		self._setter_access_tracker["ButtonFlex23"] = {}
		self._ButtonFlex23 = ButtonFlex(new_state)

	@property
	def Anchor81(self):
		self._getter_access_tracker["Anchor81"] = {}
		return self._Anchor81
	@Anchor81.setter
	def Anchor81(self, new_state):
		self._setter_access_tracker["Anchor81"] = {}
		self._Anchor81 = Anchor(new_state)

	@property
	def Image42(self):
		self._getter_access_tracker["Image42"] = {}
		return self._Image42
	@Image42.setter
	def Image42(self, new_state):
		self._setter_access_tracker["Image42"] = {}
		self._Image42 = Image(new_state)

	@property
	def ButtonFlex24(self):
		self._getter_access_tracker["ButtonFlex24"] = {}
		return self._ButtonFlex24
	@ButtonFlex24.setter
	def ButtonFlex24(self, new_state):
		self._setter_access_tracker["ButtonFlex24"] = {}
		self._ButtonFlex24 = ButtonFlex(new_state)

	@property
	def Anchor82(self):
		self._getter_access_tracker["Anchor82"] = {}
		return self._Anchor82
	@Anchor82.setter
	def Anchor82(self, new_state):
		self._setter_access_tracker["Anchor82"] = {}
		self._Anchor82 = Anchor(new_state)

	@property
	def Image43(self):
		self._getter_access_tracker["Image43"] = {}
		return self._Image43
	@Image43.setter
	def Image43(self, new_state):
		self._setter_access_tracker["Image43"] = {}
		self._Image43 = Image(new_state)

	@property
	def ButtonFlex25(self):
		self._getter_access_tracker["ButtonFlex25"] = {}
		return self._ButtonFlex25
	@ButtonFlex25.setter
	def ButtonFlex25(self, new_state):
		self._setter_access_tracker["ButtonFlex25"] = {}
		self._ButtonFlex25 = ButtonFlex(new_state)

	@property
	def Anchor83(self):
		self._getter_access_tracker["Anchor83"] = {}
		return self._Anchor83
	@Anchor83.setter
	def Anchor83(self, new_state):
		self._setter_access_tracker["Anchor83"] = {}
		self._Anchor83 = Anchor(new_state)

	@property
	def Image44(self):
		self._getter_access_tracker["Image44"] = {}
		return self._Image44
	@Image44.setter
	def Image44(self, new_state):
		self._setter_access_tracker["Image44"] = {}
		self._Image44 = Image(new_state)

	@property
	def ButtonFlex26(self):
		self._getter_access_tracker["ButtonFlex26"] = {}
		return self._ButtonFlex26
	@ButtonFlex26.setter
	def ButtonFlex26(self, new_state):
		self._setter_access_tracker["ButtonFlex26"] = {}
		self._ButtonFlex26 = ButtonFlex(new_state)

	@property
	def Anchor84(self):
		self._getter_access_tracker["Anchor84"] = {}
		return self._Anchor84
	@Anchor84.setter
	def Anchor84(self, new_state):
		self._setter_access_tracker["Anchor84"] = {}
		self._Anchor84 = Anchor(new_state)

	@property
	def Flex149(self):
		self._getter_access_tracker["Flex149"] = {}
		return self._Flex149
	@Flex149.setter
	def Flex149(self, new_state):
		self._setter_access_tracker["Flex149"] = {}
		self._Flex149 = Flex(new_state)

	@property
	def Div24(self):
		self._getter_access_tracker["Div24"] = {}
		return self._Div24
	@Div24.setter
	def Div24(self, new_state):
		self._setter_access_tracker["Div24"] = {}
		self._Div24 = Div(new_state)

	@property
	def Flex150(self):
		self._getter_access_tracker["Flex150"] = {}
		return self._Flex150
	@Flex150.setter
	def Flex150(self, new_state):
		self._setter_access_tracker["Flex150"] = {}
		self._Flex150 = Flex(new_state)

	@property
	def TextBox132(self):
		self._getter_access_tracker["TextBox132"] = {}
		return self._TextBox132
	@TextBox132.setter
	def TextBox132(self, new_state):
		self._setter_access_tracker["TextBox132"] = {}
		self._TextBox132 = TextBox(new_state)

	@property
	def Anchor85(self):
		self._getter_access_tracker["Anchor85"] = {}
		return self._Anchor85
	@Anchor85.setter
	def Anchor85(self, new_state):
		self._setter_access_tracker["Anchor85"] = {}
		self._Anchor85 = Anchor(new_state)

	@property
	def TextBox134(self):
		self._getter_access_tracker["TextBox134"] = {}
		return self._TextBox134
	@TextBox134.setter
	def TextBox134(self, new_state):
		self._setter_access_tracker["TextBox134"] = {}
		self._TextBox134 = TextBox(new_state)

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
	def Anchor87(self):
		self._getter_access_tracker["Anchor87"] = {}
		return self._Anchor87
	@Anchor87.setter
	def Anchor87(self, new_state):
		self._setter_access_tracker["Anchor87"] = {}
		self._Anchor87 = Anchor(new_state)

	@property
	def TextBox136(self):
		self._getter_access_tracker["TextBox136"] = {}
		return self._TextBox136
	@TextBox136.setter
	def TextBox136(self, new_state):
		self._setter_access_tracker["TextBox136"] = {}
		self._TextBox136 = TextBox(new_state)

	@property
	def Image45(self):
		self._getter_access_tracker["Image45"] = {}
		return self._Image45
	@Image45.setter
	def Image45(self, new_state):
		self._setter_access_tracker["Image45"] = {}
		self._Image45 = Image(new_state)

	@property
	def Anchor88(self):
		self._getter_access_tracker["Anchor88"] = {}
		return self._Anchor88
	@Anchor88.setter
	def Anchor88(self, new_state):
		self._setter_access_tracker["Anchor88"] = {}
		self._Anchor88 = Anchor(new_state)

	@property
	def TextBox137(self):
		self._getter_access_tracker["TextBox137"] = {}
		return self._TextBox137
	@TextBox137.setter
	def TextBox137(self, new_state):
		self._setter_access_tracker["TextBox137"] = {}
		self._TextBox137 = TextBox(new_state)

	@property
	def TextBox138(self):
		self._getter_access_tracker["TextBox138"] = {}
		return self._TextBox138
	@TextBox138.setter
	def TextBox138(self, new_state):
		self._setter_access_tracker["TextBox138"] = {}
		self._TextBox138 = TextBox(new_state)

	@property
	def TextBox139(self):
		self._getter_access_tracker["TextBox139"] = {}
		return self._TextBox139
	@TextBox139.setter
	def TextBox139(self, new_state):
		self._setter_access_tracker["TextBox139"] = {}
		self._TextBox139 = TextBox(new_state)

	@property
	def TextBox140(self):
		self._getter_access_tracker["TextBox140"] = {}
		return self._TextBox140
	@TextBox140.setter
	def TextBox140(self, new_state):
		self._setter_access_tracker["TextBox140"] = {}
		self._TextBox140 = TextBox(new_state)

	@property
	def TextBox141(self):
		self._getter_access_tracker["TextBox141"] = {}
		return self._TextBox141
	@TextBox141.setter
	def TextBox141(self, new_state):
		self._setter_access_tracker["TextBox141"] = {}
		self._TextBox141 = TextBox(new_state)

	@property
	def TextBox142(self):
		self._getter_access_tracker["TextBox142"] = {}
		return self._TextBox142
	@TextBox142.setter
	def TextBox142(self, new_state):
		self._setter_access_tracker["TextBox142"] = {}
		self._TextBox142 = TextBox(new_state)

	@property
	def LineText1(self):
		self._getter_access_tracker["LineText1"] = {}
		return self._LineText1
	@LineText1.setter
	def LineText1(self, new_state):
		self._setter_access_tracker["LineText1"] = {}
		self._LineText1 = LineText(new_state)

	@property
	def LineText2(self):
		self._getter_access_tracker["LineText2"] = {}
		return self._LineText2
	@LineText2.setter
	def LineText2(self, new_state):
		self._setter_access_tracker["LineText2"] = {}
		self._LineText2 = LineText(new_state)

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
	def ButtonFlex27(self):
		self._getter_access_tracker["ButtonFlex27"] = {}
		return self._ButtonFlex27
	@ButtonFlex27.setter
	def ButtonFlex27(self, new_state):
		self._setter_access_tracker["ButtonFlex27"] = {}
		self._ButtonFlex27 = ButtonFlex(new_state)

	@property
	def Flex151(self):
		self._getter_access_tracker["Flex151"] = {}
		return self._Flex151
	@Flex151.setter
	def Flex151(self, new_state):
		self._setter_access_tracker["Flex151"] = {}
		self._Flex151 = Flex(new_state)

	@property
	def Flex152(self):
		self._getter_access_tracker["Flex152"] = {}
		return self._Flex152
	@Flex152.setter
	def Flex152(self, new_state):
		self._setter_access_tracker["Flex152"] = {}
		self._Flex152 = Flex(new_state)

	@property
	def TextBox143(self):
		self._getter_access_tracker["TextBox143"] = {}
		return self._TextBox143
	@TextBox143.setter
	def TextBox143(self, new_state):
		self._setter_access_tracker["TextBox143"] = {}
		self._TextBox143 = TextBox(new_state)

	@property
	def Flex153(self):
		self._getter_access_tracker["Flex153"] = {}
		return self._Flex153
	@Flex153.setter
	def Flex153(self, new_state):
		self._setter_access_tracker["Flex153"] = {}
		self._Flex153 = Flex(new_state)

	@property
	def TextBox144(self):
		self._getter_access_tracker["TextBox144"] = {}
		return self._TextBox144
	@TextBox144.setter
	def TextBox144(self, new_state):
		self._setter_access_tracker["TextBox144"] = {}
		self._TextBox144 = TextBox(new_state)

	@property
	def TextBox145(self):
		self._getter_access_tracker["TextBox145"] = {}
		return self._TextBox145
	@TextBox145.setter
	def TextBox145(self, new_state):
		self._setter_access_tracker["TextBox145"] = {}
		self._TextBox145 = TextBox(new_state)

	@property
	def Flex154(self):
		self._getter_access_tracker["Flex154"] = {}
		return self._Flex154
	@Flex154.setter
	def Flex154(self, new_state):
		self._setter_access_tracker["Flex154"] = {}
		self._Flex154 = Flex(new_state)

	@property
	def Image46(self):
		self._getter_access_tracker["Image46"] = {}
		return self._Image46
	@Image46.setter
	def Image46(self, new_state):
		self._setter_access_tracker["Image46"] = {}
		self._Image46 = Image(new_state)

	@property
	def TextBox146(self):
		self._getter_access_tracker["TextBox146"] = {}
		return self._TextBox146
	@TextBox146.setter
	def TextBox146(self, new_state):
		self._setter_access_tracker["TextBox146"] = {}
		self._TextBox146 = TextBox(new_state)

	@property
	def TextBox147(self):
		self._getter_access_tracker["TextBox147"] = {}
		return self._TextBox147
	@TextBox147.setter
	def TextBox147(self, new_state):
		self._setter_access_tracker["TextBox147"] = {}
		self._TextBox147 = TextBox(new_state)

	@property
	def Image47(self):
		self._getter_access_tracker["Image47"] = {}
		return self._Image47
	@Image47.setter
	def Image47(self, new_state):
		self._setter_access_tracker["Image47"] = {}
		self._Image47 = Image(new_state)

	@property
	def Flex155(self):
		self._getter_access_tracker["Flex155"] = {}
		return self._Flex155
	@Flex155.setter
	def Flex155(self, new_state):
		self._setter_access_tracker["Flex155"] = {}
		self._Flex155 = Flex(new_state)

	@property
	def TextBox148(self):
		self._getter_access_tracker["TextBox148"] = {}
		return self._TextBox148
	@TextBox148.setter
	def TextBox148(self, new_state):
		self._setter_access_tracker["TextBox148"] = {}
		self._TextBox148 = TextBox(new_state)

	@property
	def Flex156(self):
		self._getter_access_tracker["Flex156"] = {}
		return self._Flex156
	@Flex156.setter
	def Flex156(self, new_state):
		self._setter_access_tracker["Flex156"] = {}
		self._Flex156 = Flex(new_state)

	@property
	def Flex157(self):
		self._getter_access_tracker["Flex157"] = {}
		return self._Flex157
	@Flex157.setter
	def Flex157(self, new_state):
		self._setter_access_tracker["Flex157"] = {}
		self._Flex157 = Flex(new_state)

	@property
	def Flex158(self):
		self._getter_access_tracker["Flex158"] = {}
		return self._Flex158
	@Flex158.setter
	def Flex158(self, new_state):
		self._setter_access_tracker["Flex158"] = {}
		self._Flex158 = Flex(new_state)

	@property
	def ButtonFlex28(self):
		self._getter_access_tracker["ButtonFlex28"] = {}
		return self._ButtonFlex28
	@ButtonFlex28.setter
	def ButtonFlex28(self, new_state):
		self._setter_access_tracker["ButtonFlex28"] = {}
		self._ButtonFlex28 = ButtonFlex(new_state)

	@property
	def Anchor91(self):
		self._getter_access_tracker["Anchor91"] = {}
		return self._Anchor91
	@Anchor91.setter
	def Anchor91(self, new_state):
		self._setter_access_tracker["Anchor91"] = {}
		self._Anchor91 = Anchor(new_state)

	@property
	def Flex159(self):
		self._getter_access_tracker["Flex159"] = {}
		return self._Flex159
	@Flex159.setter
	def Flex159(self, new_state):
		self._setter_access_tracker["Flex159"] = {}
		self._Flex159 = Flex(new_state)

	@property
	def FramerFlex19(self):
		self._getter_access_tracker["FramerFlex19"] = {}
		return self._FramerFlex19
	@FramerFlex19.setter
	def FramerFlex19(self, new_state):
		self._setter_access_tracker["FramerFlex19"] = {}
		self._FramerFlex19 = FramerFlex(new_state)

	@property
	def TextBox149(self):
		self._getter_access_tracker["TextBox149"] = {}
		return self._TextBox149
	@TextBox149.setter
	def TextBox149(self, new_state):
		self._setter_access_tracker["TextBox149"] = {}
		self._TextBox149 = TextBox(new_state)

	@property
	def TextBox150(self):
		self._getter_access_tracker["TextBox150"] = {}
		return self._TextBox150
	@TextBox150.setter
	def TextBox150(self, new_state):
		self._setter_access_tracker["TextBox150"] = {}
		self._TextBox150 = TextBox(new_state)

	@property
	def Image48(self):
		self._getter_access_tracker["Image48"] = {}
		return self._Image48
	@Image48.setter
	def Image48(self, new_state):
		self._setter_access_tracker["Image48"] = {}
		self._Image48 = Image(new_state)

	@property
	def Flex161(self):
		self._getter_access_tracker["Flex161"] = {}
		return self._Flex161
	@Flex161.setter
	def Flex161(self, new_state):
		self._setter_access_tracker["Flex161"] = {}
		self._Flex161 = Flex(new_state)

	@property
	def TextBox151(self):
		self._getter_access_tracker["TextBox151"] = {}
		return self._TextBox151
	@TextBox151.setter
	def TextBox151(self, new_state):
		self._setter_access_tracker["TextBox151"] = {}
		self._TextBox151 = TextBox(new_state)

	@property
	def Flex162(self):
		self._getter_access_tracker["Flex162"] = {}
		return self._Flex162
	@Flex162.setter
	def Flex162(self, new_state):
		self._setter_access_tracker["Flex162"] = {}
		self._Flex162 = Flex(new_state)

	@property
	def Flex163(self):
		self._getter_access_tracker["Flex163"] = {}
		return self._Flex163
	@Flex163.setter
	def Flex163(self, new_state):
		self._setter_access_tracker["Flex163"] = {}
		self._Flex163 = Flex(new_state)

	@property
	def Flex164(self):
		self._getter_access_tracker["Flex164"] = {}
		return self._Flex164
	@Flex164.setter
	def Flex164(self, new_state):
		self._setter_access_tracker["Flex164"] = {}
		self._Flex164 = Flex(new_state)

	@property
	def ButtonFlex29(self):
		self._getter_access_tracker["ButtonFlex29"] = {}
		return self._ButtonFlex29
	@ButtonFlex29.setter
	def ButtonFlex29(self, new_state):
		self._setter_access_tracker["ButtonFlex29"] = {}
		self._ButtonFlex29 = ButtonFlex(new_state)

	@property
	def Anchor92(self):
		self._getter_access_tracker["Anchor92"] = {}
		return self._Anchor92
	@Anchor92.setter
	def Anchor92(self, new_state):
		self._setter_access_tracker["Anchor92"] = {}
		self._Anchor92 = Anchor(new_state)

	@property
	def TextBox152(self):
		self._getter_access_tracker["TextBox152"] = {}
		return self._TextBox152
	@TextBox152.setter
	def TextBox152(self, new_state):
		self._setter_access_tracker["TextBox152"] = {}
		self._TextBox152 = TextBox(new_state)

	@property
	def TextBox153(self):
		self._getter_access_tracker["TextBox153"] = {}
		return self._TextBox153
	@TextBox153.setter
	def TextBox153(self, new_state):
		self._setter_access_tracker["TextBox153"] = {}
		self._TextBox153 = TextBox(new_state)

	@property
	def Image49(self):
		self._getter_access_tracker["Image49"] = {}
		return self._Image49
	@Image49.setter
	def Image49(self, new_state):
		self._setter_access_tracker["Image49"] = {}
		self._Image49 = Image(new_state)

	@property
	def Flex165(self):
		self._getter_access_tracker["Flex165"] = {}
		return self._Flex165
	@Flex165.setter
	def Flex165(self, new_state):
		self._setter_access_tracker["Flex165"] = {}
		self._Flex165 = Flex(new_state)

	@property
	def TextBox154(self):
		self._getter_access_tracker["TextBox154"] = {}
		return self._TextBox154
	@TextBox154.setter
	def TextBox154(self, new_state):
		self._setter_access_tracker["TextBox154"] = {}
		self._TextBox154 = TextBox(new_state)

	@property
	def Flex166(self):
		self._getter_access_tracker["Flex166"] = {}
		return self._Flex166
	@Flex166.setter
	def Flex166(self, new_state):
		self._setter_access_tracker["Flex166"] = {}
		self._Flex166 = Flex(new_state)

	@property
	def Flex167(self):
		self._getter_access_tracker["Flex167"] = {}
		return self._Flex167
	@Flex167.setter
	def Flex167(self, new_state):
		self._setter_access_tracker["Flex167"] = {}
		self._Flex167 = Flex(new_state)

	@property
	def Flex168(self):
		self._getter_access_tracker["Flex168"] = {}
		return self._Flex168
	@Flex168.setter
	def Flex168(self, new_state):
		self._setter_access_tracker["Flex168"] = {}
		self._Flex168 = Flex(new_state)

	@property
	def ButtonFlex30(self):
		self._getter_access_tracker["ButtonFlex30"] = {}
		return self._ButtonFlex30
	@ButtonFlex30.setter
	def ButtonFlex30(self, new_state):
		self._setter_access_tracker["ButtonFlex30"] = {}
		self._ButtonFlex30 = ButtonFlex(new_state)

	@property
	def Anchor93(self):
		self._getter_access_tracker["Anchor93"] = {}
		return self._Anchor93
	@Anchor93.setter
	def Anchor93(self, new_state):
		self._setter_access_tracker["Anchor93"] = {}
		self._Anchor93 = Anchor(new_state)

	@property
	def TextBox155(self):
		self._getter_access_tracker["TextBox155"] = {}
		return self._TextBox155
	@TextBox155.setter
	def TextBox155(self, new_state):
		self._setter_access_tracker["TextBox155"] = {}
		self._TextBox155 = TextBox(new_state)

	@property
	def TextBox156(self):
		self._getter_access_tracker["TextBox156"] = {}
		return self._TextBox156
	@TextBox156.setter
	def TextBox156(self, new_state):
		self._setter_access_tracker["TextBox156"] = {}
		self._TextBox156 = TextBox(new_state)

	@property
	def Image50(self):
		self._getter_access_tracker["Image50"] = {}
		return self._Image50
	@Image50.setter
	def Image50(self, new_state):
		self._setter_access_tracker["Image50"] = {}
		self._Image50 = Image(new_state)

	@property
	def Flex169(self):
		self._getter_access_tracker["Flex169"] = {}
		return self._Flex169
	@Flex169.setter
	def Flex169(self, new_state):
		self._setter_access_tracker["Flex169"] = {}
		self._Flex169 = Flex(new_state)

	@property
	def TextBox157(self):
		self._getter_access_tracker["TextBox157"] = {}
		return self._TextBox157
	@TextBox157.setter
	def TextBox157(self, new_state):
		self._setter_access_tracker["TextBox157"] = {}
		self._TextBox157 = TextBox(new_state)

	@property
	def Flex170(self):
		self._getter_access_tracker["Flex170"] = {}
		return self._Flex170
	@Flex170.setter
	def Flex170(self, new_state):
		self._setter_access_tracker["Flex170"] = {}
		self._Flex170 = Flex(new_state)

	@property
	def Flex171(self):
		self._getter_access_tracker["Flex171"] = {}
		return self._Flex171
	@Flex171.setter
	def Flex171(self, new_state):
		self._setter_access_tracker["Flex171"] = {}
		self._Flex171 = Flex(new_state)

	@property
	def Flex172(self):
		self._getter_access_tracker["Flex172"] = {}
		return self._Flex172
	@Flex172.setter
	def Flex172(self, new_state):
		self._setter_access_tracker["Flex172"] = {}
		self._Flex172 = Flex(new_state)

	@property
	def ButtonFlex31(self):
		self._getter_access_tracker["ButtonFlex31"] = {}
		return self._ButtonFlex31
	@ButtonFlex31.setter
	def ButtonFlex31(self, new_state):
		self._setter_access_tracker["ButtonFlex31"] = {}
		self._ButtonFlex31 = ButtonFlex(new_state)

	@property
	def Anchor94(self):
		self._getter_access_tracker["Anchor94"] = {}
		return self._Anchor94
	@Anchor94.setter
	def Anchor94(self, new_state):
		self._setter_access_tracker["Anchor94"] = {}
		self._Anchor94 = Anchor(new_state)

	@property
	def Anchor95(self):
		self._getter_access_tracker["Anchor95"] = {}
		return self._Anchor95
	@Anchor95.setter
	def Anchor95(self, new_state):
		self._setter_access_tracker["Anchor95"] = {}
		self._Anchor95 = Anchor(new_state)

	@property
	def LineText3(self):
		self._getter_access_tracker["LineText3"] = {}
		return self._LineText3
	@LineText3.setter
	def LineText3(self, new_state):
		self._setter_access_tracker["LineText3"] = {}
		self._LineText3 = LineText(new_state)

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
	def FramerText46(self):
		self._getter_access_tracker["FramerText46"] = {}
		return self._FramerText46
	@FramerText46.setter
	def FramerText46(self, new_state):
		self._setter_access_tracker["FramerText46"] = {}
		self._FramerText46 = FramerText(new_state)

	@property
	def FramerText47(self):
		self._getter_access_tracker["FramerText47"] = {}
		return self._FramerText47
	@FramerText47.setter
	def FramerText47(self, new_state):
		self._setter_access_tracker["FramerText47"] = {}
		self._FramerText47 = FramerText(new_state)

	@property
	def FramerText48(self):
		self._getter_access_tracker["FramerText48"] = {}
		return self._FramerText48
	@FramerText48.setter
	def FramerText48(self, new_state):
		self._setter_access_tracker["FramerText48"] = {}
		self._FramerText48 = FramerText(new_state)

	@property
	def FramerText49(self):
		self._getter_access_tracker["FramerText49"] = {}
		return self._FramerText49
	@FramerText49.setter
	def FramerText49(self, new_state):
		self._setter_access_tracker["FramerText49"] = {}
		self._FramerText49 = FramerText(new_state)

	@property
	def FramerText50(self):
		self._getter_access_tracker["FramerText50"] = {}
		return self._FramerText50
	@FramerText50.setter
	def FramerText50(self, new_state):
		self._setter_access_tracker["FramerText50"] = {}
		self._FramerText50 = FramerText(new_state)

	@property
	def FramerText51(self):
		self._getter_access_tracker["FramerText51"] = {}
		return self._FramerText51
	@FramerText51.setter
	def FramerText51(self, new_state):
		self._setter_access_tracker["FramerText51"] = {}
		self._FramerText51 = FramerText(new_state)

	@property
	def FramerText52(self):
		self._getter_access_tracker["FramerText52"] = {}
		return self._FramerText52
	@FramerText52.setter
	def FramerText52(self, new_state):
		self._setter_access_tracker["FramerText52"] = {}
		self._FramerText52 = FramerText(new_state)

	@property
	def FramerText53(self):
		self._getter_access_tracker["FramerText53"] = {}
		return self._FramerText53
	@FramerText53.setter
	def FramerText53(self, new_state):
		self._setter_access_tracker["FramerText53"] = {}
		self._FramerText53 = FramerText(new_state)

	@property
	def FramerText54(self):
		self._getter_access_tracker["FramerText54"] = {}
		return self._FramerText54
	@FramerText54.setter
	def FramerText54(self, new_state):
		self._setter_access_tracker["FramerText54"] = {}
		self._FramerText54 = FramerText(new_state)

	@property
	def FramerText55(self):
		self._getter_access_tracker["FramerText55"] = {}
		return self._FramerText55
	@FramerText55.setter
	def FramerText55(self, new_state):
		self._setter_access_tracker["FramerText55"] = {}
		self._FramerText55 = FramerText(new_state)

	@property
	def FramerText56(self):
		self._getter_access_tracker["FramerText56"] = {}
		return self._FramerText56
	@FramerText56.setter
	def FramerText56(self, new_state):
		self._setter_access_tracker["FramerText56"] = {}
		self._FramerText56 = FramerText(new_state)

	@property
	def FramerText57(self):
		self._getter_access_tracker["FramerText57"] = {}
		return self._FramerText57
	@FramerText57.setter
	def FramerText57(self, new_state):
		self._setter_access_tracker["FramerText57"] = {}
		self._FramerText57 = FramerText(new_state)

	@property
	def FramerText58(self):
		self._getter_access_tracker["FramerText58"] = {}
		return self._FramerText58
	@FramerText58.setter
	def FramerText58(self, new_state):
		self._setter_access_tracker["FramerText58"] = {}
		self._FramerText58 = FramerText(new_state)

	@property
	def FramerText59(self):
		self._getter_access_tracker["FramerText59"] = {}
		return self._FramerText59
	@FramerText59.setter
	def FramerText59(self, new_state):
		self._setter_access_tracker["FramerText59"] = {}
		self._FramerText59 = FramerText(new_state)

	@property
	def FramerText60(self):
		self._getter_access_tracker["FramerText60"] = {}
		return self._FramerText60
	@FramerText60.setter
	def FramerText60(self, new_state):
		self._setter_access_tracker["FramerText60"] = {}
		self._FramerText60 = FramerText(new_state)

	@property
	def FramerText61(self):
		self._getter_access_tracker["FramerText61"] = {}
		return self._FramerText61
	@FramerText61.setter
	def FramerText61(self, new_state):
		self._setter_access_tracker["FramerText61"] = {}
		self._FramerText61 = FramerText(new_state)

	@property
	def FramerText62(self):
		self._getter_access_tracker["FramerText62"] = {}
		return self._FramerText62
	@FramerText62.setter
	def FramerText62(self, new_state):
		self._setter_access_tracker["FramerText62"] = {}
		self._FramerText62 = FramerText(new_state)

	@property
	def FramerText63(self):
		self._getter_access_tracker["FramerText63"] = {}
		return self._FramerText63
	@FramerText63.setter
	def FramerText63(self, new_state):
		self._setter_access_tracker["FramerText63"] = {}
		self._FramerText63 = FramerText(new_state)

	@property
	def FramerText64(self):
		self._getter_access_tracker["FramerText64"] = {}
		return self._FramerText64
	@FramerText64.setter
	def FramerText64(self, new_state):
		self._setter_access_tracker["FramerText64"] = {}
		self._FramerText64 = FramerText(new_state)

	@property
	def FramerText65(self):
		self._getter_access_tracker["FramerText65"] = {}
		return self._FramerText65
	@FramerText65.setter
	def FramerText65(self, new_state):
		self._setter_access_tracker["FramerText65"] = {}
		self._FramerText65 = FramerText(new_state)

	@property
	def FramerText66(self):
		self._getter_access_tracker["FramerText66"] = {}
		return self._FramerText66
	@FramerText66.setter
	def FramerText66(self, new_state):
		self._setter_access_tracker["FramerText66"] = {}
		self._FramerText66 = FramerText(new_state)

	@property
	def FramerText67(self):
		self._getter_access_tracker["FramerText67"] = {}
		return self._FramerText67
	@FramerText67.setter
	def FramerText67(self, new_state):
		self._setter_access_tracker["FramerText67"] = {}
		self._FramerText67 = FramerText(new_state)

	@property
	def FramerText68(self):
		self._getter_access_tracker["FramerText68"] = {}
		return self._FramerText68
	@FramerText68.setter
	def FramerText68(self, new_state):
		self._setter_access_tracker["FramerText68"] = {}
		self._FramerText68 = FramerText(new_state)

	@property
	def Anchor97(self):
		self._getter_access_tracker["Anchor97"] = {}
		return self._Anchor97
	@Anchor97.setter
	def Anchor97(self, new_state):
		self._setter_access_tracker["Anchor97"] = {}
		self._Anchor97 = Anchor(new_state)

	@property
	def Anchor98(self):
		self._getter_access_tracker["Anchor98"] = {}
		return self._Anchor98
	@Anchor98.setter
	def Anchor98(self, new_state):
		self._setter_access_tracker["Anchor98"] = {}
		self._Anchor98 = Anchor(new_state)

	@property
	def Anchor99(self):
		self._getter_access_tracker["Anchor99"] = {}
		return self._Anchor99
	@Anchor99.setter
	def Anchor99(self, new_state):
		self._setter_access_tracker["Anchor99"] = {}
		self._Anchor99 = Anchor(new_state)

	@property
	def Anchor100(self):
		self._getter_access_tracker["Anchor100"] = {}
		return self._Anchor100
	@Anchor100.setter
	def Anchor100(self, new_state):
		self._setter_access_tracker["Anchor100"] = {}
		self._Anchor100 = Anchor(new_state)

	@property
	def Anchor101(self):
		self._getter_access_tracker["Anchor101"] = {}
		return self._Anchor101
	@Anchor101.setter
	def Anchor101(self, new_state):
		self._setter_access_tracker["Anchor101"] = {}
		self._Anchor101 = Anchor(new_state)

	@property
	def Anchor102(self):
		self._getter_access_tracker["Anchor102"] = {}
		return self._Anchor102
	@Anchor102.setter
	def Anchor102(self, new_state):
		self._setter_access_tracker["Anchor102"] = {}
		self._Anchor102 = Anchor(new_state)

	@property
	def Anchor103(self):
		self._getter_access_tracker["Anchor103"] = {}
		return self._Anchor103
	@Anchor103.setter
	def Anchor103(self, new_state):
		self._setter_access_tracker["Anchor103"] = {}
		self._Anchor103 = Anchor(new_state)

	@property
	def Anchor104(self):
		self._getter_access_tracker["Anchor104"] = {}
		return self._Anchor104
	@Anchor104.setter
	def Anchor104(self, new_state):
		self._setter_access_tracker["Anchor104"] = {}
		self._Anchor104 = Anchor(new_state)

	@property
	def Anchor105(self):
		self._getter_access_tracker["Anchor105"] = {}
		return self._Anchor105
	@Anchor105.setter
	def Anchor105(self, new_state):
		self._setter_access_tracker["Anchor105"] = {}
		self._Anchor105 = Anchor(new_state)

	@property
	def Anchor106(self):
		self._getter_access_tracker["Anchor106"] = {}
		return self._Anchor106
	@Anchor106.setter
	def Anchor106(self, new_state):
		self._setter_access_tracker["Anchor106"] = {}
		self._Anchor106 = Anchor(new_state)

	@property
	def Anchor107(self):
		self._getter_access_tracker["Anchor107"] = {}
		return self._Anchor107
	@Anchor107.setter
	def Anchor107(self, new_state):
		self._setter_access_tracker["Anchor107"] = {}
		self._Anchor107 = Anchor(new_state)

	@property
	def Anchor108(self):
		self._getter_access_tracker["Anchor108"] = {}
		return self._Anchor108
	@Anchor108.setter
	def Anchor108(self, new_state):
		self._setter_access_tracker["Anchor108"] = {}
		self._Anchor108 = Anchor(new_state)

	@property
	def Anchor109(self):
		self._getter_access_tracker["Anchor109"] = {}
		return self._Anchor109
	@Anchor109.setter
	def Anchor109(self, new_state):
		self._setter_access_tracker["Anchor109"] = {}
		self._Anchor109 = Anchor(new_state)

	@property
	def Anchor110(self):
		self._getter_access_tracker["Anchor110"] = {}
		return self._Anchor110
	@Anchor110.setter
	def Anchor110(self, new_state):
		self._setter_access_tracker["Anchor110"] = {}
		self._Anchor110 = Anchor(new_state)

	@property
	def Anchor111(self):
		self._getter_access_tracker["Anchor111"] = {}
		return self._Anchor111
	@Anchor111.setter
	def Anchor111(self, new_state):
		self._setter_access_tracker["Anchor111"] = {}
		self._Anchor111 = Anchor(new_state)

	@property
	def Anchor112(self):
		self._getter_access_tracker["Anchor112"] = {}
		return self._Anchor112
	@Anchor112.setter
	def Anchor112(self, new_state):
		self._setter_access_tracker["Anchor112"] = {}
		self._Anchor112 = Anchor(new_state)

	@property
	def Anchor113(self):
		self._getter_access_tracker["Anchor113"] = {}
		return self._Anchor113
	@Anchor113.setter
	def Anchor113(self, new_state):
		self._setter_access_tracker["Anchor113"] = {}
		self._Anchor113 = Anchor(new_state)

	@property
	def Anchor114(self):
		self._getter_access_tracker["Anchor114"] = {}
		return self._Anchor114
	@Anchor114.setter
	def Anchor114(self, new_state):
		self._setter_access_tracker["Anchor114"] = {}
		self._Anchor114 = Anchor(new_state)

	@property
	def Anchor115(self):
		self._getter_access_tracker["Anchor115"] = {}
		return self._Anchor115
	@Anchor115.setter
	def Anchor115(self, new_state):
		self._setter_access_tracker["Anchor115"] = {}
		self._Anchor115 = Anchor(new_state)

	@property
	def Anchor116(self):
		self._getter_access_tracker["Anchor116"] = {}
		return self._Anchor116
	@Anchor116.setter
	def Anchor116(self, new_state):
		self._setter_access_tracker["Anchor116"] = {}
		self._Anchor116 = Anchor(new_state)

	@property
	def Anchor117(self):
		self._getter_access_tracker["Anchor117"] = {}
		return self._Anchor117
	@Anchor117.setter
	def Anchor117(self, new_state):
		self._setter_access_tracker["Anchor117"] = {}
		self._Anchor117 = Anchor(new_state)

	@property
	def Anchor118(self):
		self._getter_access_tracker["Anchor118"] = {}
		return self._Anchor118
	@Anchor118.setter
	def Anchor118(self, new_state):
		self._setter_access_tracker["Anchor118"] = {}
		self._Anchor118 = Anchor(new_state)

	@property
	def Anchor119(self):
		self._getter_access_tracker["Anchor119"] = {}
		return self._Anchor119
	@Anchor119.setter
	def Anchor119(self, new_state):
		self._setter_access_tracker["Anchor119"] = {}
		self._Anchor119 = Anchor(new_state)

	@property
	def Flex173(self):
		self._getter_access_tracker["Flex173"] = {}
		return self._Flex173
	@Flex173.setter
	def Flex173(self, new_state):
		self._setter_access_tracker["Flex173"] = {}
		self._Flex173 = Flex(new_state)

	@property
	def Flex174(self):
		self._getter_access_tracker["Flex174"] = {}
		return self._Flex174
	@Flex174.setter
	def Flex174(self, new_state):
		self._setter_access_tracker["Flex174"] = {}
		self._Flex174 = Flex(new_state)

	@property
	def Flex175(self):
		self._getter_access_tracker["Flex175"] = {}
		return self._Flex175
	@Flex175.setter
	def Flex175(self, new_state):
		self._setter_access_tracker["Flex175"] = {}
		self._Flex175 = Flex(new_state)

	@property
	def TextBox158(self):
		self._getter_access_tracker["TextBox158"] = {}
		return self._TextBox158
	@TextBox158.setter
	def TextBox158(self, new_state):
		self._setter_access_tracker["TextBox158"] = {}
		self._TextBox158 = TextBox(new_state)

	@property
	def Flex176(self):
		self._getter_access_tracker["Flex176"] = {}
		return self._Flex176
	@Flex176.setter
	def Flex176(self, new_state):
		self._setter_access_tracker["Flex176"] = {}
		self._Flex176 = Flex(new_state)

	@property
	def FramerText69(self):
		self._getter_access_tracker["FramerText69"] = {}
		return self._FramerText69
	@FramerText69.setter
	def FramerText69(self, new_state):
		self._setter_access_tracker["FramerText69"] = {}
		self._FramerText69 = FramerText(new_state)

	@property
	def FramerText70(self):
		self._getter_access_tracker["FramerText70"] = {}
		return self._FramerText70
	@FramerText70.setter
	def FramerText70(self, new_state):
		self._setter_access_tracker["FramerText70"] = {}
		self._FramerText70 = FramerText(new_state)

	@property
	def FramerText71(self):
		self._getter_access_tracker["FramerText71"] = {}
		return self._FramerText71
	@FramerText71.setter
	def FramerText71(self, new_state):
		self._setter_access_tracker["FramerText71"] = {}
		self._FramerText71 = FramerText(new_state)

	@property
	def FramerText72(self):
		self._getter_access_tracker["FramerText72"] = {}
		return self._FramerText72
	@FramerText72.setter
	def FramerText72(self, new_state):
		self._setter_access_tracker["FramerText72"] = {}
		self._FramerText72 = FramerText(new_state)

	@property
	def FramerText73(self):
		self._getter_access_tracker["FramerText73"] = {}
		return self._FramerText73
	@FramerText73.setter
	def FramerText73(self, new_state):
		self._setter_access_tracker["FramerText73"] = {}
		self._FramerText73 = FramerText(new_state)

	@property
	def FramerText74(self):
		self._getter_access_tracker["FramerText74"] = {}
		return self._FramerText74
	@FramerText74.setter
	def FramerText74(self, new_state):
		self._setter_access_tracker["FramerText74"] = {}
		self._FramerText74 = FramerText(new_state)

	@property
	def Anchor120(self):
		self._getter_access_tracker["Anchor120"] = {}
		return self._Anchor120
	@Anchor120.setter
	def Anchor120(self, new_state):
		self._setter_access_tracker["Anchor120"] = {}
		self._Anchor120 = Anchor(new_state)

	@property
	def Anchor121(self):
		self._getter_access_tracker["Anchor121"] = {}
		return self._Anchor121
	@Anchor121.setter
	def Anchor121(self, new_state):
		self._setter_access_tracker["Anchor121"] = {}
		self._Anchor121 = Anchor(new_state)

	@property
	def Anchor122(self):
		self._getter_access_tracker["Anchor122"] = {}
		return self._Anchor122
	@Anchor122.setter
	def Anchor122(self, new_state):
		self._setter_access_tracker["Anchor122"] = {}
		self._Anchor122 = Anchor(new_state)

	@property
	def Anchor123(self):
		self._getter_access_tracker["Anchor123"] = {}
		return self._Anchor123
	@Anchor123.setter
	def Anchor123(self, new_state):
		self._setter_access_tracker["Anchor123"] = {}
		self._Anchor123 = Anchor(new_state)

	@property
	def Anchor124(self):
		self._getter_access_tracker["Anchor124"] = {}
		return self._Anchor124
	@Anchor124.setter
	def Anchor124(self, new_state):
		self._setter_access_tracker["Anchor124"] = {}
		self._Anchor124 = Anchor(new_state)

	@property
	def Anchor125(self):
		self._getter_access_tracker["Anchor125"] = {}
		return self._Anchor125
	@Anchor125.setter
	def Anchor125(self, new_state):
		self._setter_access_tracker["Anchor125"] = {}
		self._Anchor125 = Anchor(new_state)

	@property
	def TextBox159(self):
		self._getter_access_tracker["TextBox159"] = {}
		return self._TextBox159
	@TextBox159.setter
	def TextBox159(self, new_state):
		self._setter_access_tracker["TextBox159"] = {}
		self._TextBox159 = TextBox(new_state)

	@property
	def Flex177(self):
		self._getter_access_tracker["Flex177"] = {}
		return self._Flex177
	@Flex177.setter
	def Flex177(self, new_state):
		self._setter_access_tracker["Flex177"] = {}
		self._Flex177 = Flex(new_state)

	@property
	def Flex178(self):
		self._getter_access_tracker["Flex178"] = {}
		return self._Flex178
	@Flex178.setter
	def Flex178(self, new_state):
		self._setter_access_tracker["Flex178"] = {}
		self._Flex178 = Flex(new_state)

	@property
	def Flex179(self):
		self._getter_access_tracker["Flex179"] = {}
		return self._Flex179
	@Flex179.setter
	def Flex179(self, new_state):
		self._setter_access_tracker["Flex179"] = {}
		self._Flex179 = Flex(new_state)

	@property
	def LineText4(self):
		self._getter_access_tracker["LineText4"] = {}
		return self._LineText4
	@LineText4.setter
	def LineText4(self, new_state):
		self._setter_access_tracker["LineText4"] = {}
		self._LineText4 = LineText(new_state)

	@property
	def FramerText75(self):
		self._getter_access_tracker["FramerText75"] = {}
		return self._FramerText75
	@FramerText75.setter
	def FramerText75(self, new_state):
		self._setter_access_tracker["FramerText75"] = {}
		self._FramerText75 = FramerText(new_state)

	@property
	def FramerText76(self):
		self._getter_access_tracker["FramerText76"] = {}
		return self._FramerText76
	@FramerText76.setter
	def FramerText76(self, new_state):
		self._setter_access_tracker["FramerText76"] = {}
		self._FramerText76 = FramerText(new_state)

	@property
	def FramerText77(self):
		self._getter_access_tracker["FramerText77"] = {}
		return self._FramerText77
	@FramerText77.setter
	def FramerText77(self, new_state):
		self._setter_access_tracker["FramerText77"] = {}
		self._FramerText77 = FramerText(new_state)

	@property
	def FramerText78(self):
		self._getter_access_tracker["FramerText78"] = {}
		return self._FramerText78
	@FramerText78.setter
	def FramerText78(self, new_state):
		self._setter_access_tracker["FramerText78"] = {}
		self._FramerText78 = FramerText(new_state)

	@property
	def FramerText79(self):
		self._getter_access_tracker["FramerText79"] = {}
		return self._FramerText79
	@FramerText79.setter
	def FramerText79(self, new_state):
		self._setter_access_tracker["FramerText79"] = {}
		self._FramerText79 = FramerText(new_state)

	@property
	def FramerText80(self):
		self._getter_access_tracker["FramerText80"] = {}
		return self._FramerText80
	@FramerText80.setter
	def FramerText80(self, new_state):
		self._setter_access_tracker["FramerText80"] = {}
		self._FramerText80 = FramerText(new_state)

	@property
	def Anchor126(self):
		self._getter_access_tracker["Anchor126"] = {}
		return self._Anchor126
	@Anchor126.setter
	def Anchor126(self, new_state):
		self._setter_access_tracker["Anchor126"] = {}
		self._Anchor126 = Anchor(new_state)

	@property
	def Anchor127(self):
		self._getter_access_tracker["Anchor127"] = {}
		return self._Anchor127
	@Anchor127.setter
	def Anchor127(self, new_state):
		self._setter_access_tracker["Anchor127"] = {}
		self._Anchor127 = Anchor(new_state)

	@property
	def Anchor128(self):
		self._getter_access_tracker["Anchor128"] = {}
		return self._Anchor128
	@Anchor128.setter
	def Anchor128(self, new_state):
		self._setter_access_tracker["Anchor128"] = {}
		self._Anchor128 = Anchor(new_state)

	@property
	def Anchor129(self):
		self._getter_access_tracker["Anchor129"] = {}
		return self._Anchor129
	@Anchor129.setter
	def Anchor129(self, new_state):
		self._setter_access_tracker["Anchor129"] = {}
		self._Anchor129 = Anchor(new_state)

	@property
	def Anchor130(self):
		self._getter_access_tracker["Anchor130"] = {}
		return self._Anchor130
	@Anchor130.setter
	def Anchor130(self, new_state):
		self._setter_access_tracker["Anchor130"] = {}
		self._Anchor130 = Anchor(new_state)

	@property
	def Anchor131(self):
		self._getter_access_tracker["Anchor131"] = {}
		return self._Anchor131
	@Anchor131.setter
	def Anchor131(self, new_state):
		self._setter_access_tracker["Anchor131"] = {}
		self._Anchor131 = Anchor(new_state)

	@property
	def Anchor132(self):
		self._getter_access_tracker["Anchor132"] = {}
		return self._Anchor132
	@Anchor132.setter
	def Anchor132(self, new_state):
		self._setter_access_tracker["Anchor132"] = {}
		self._Anchor132 = Anchor(new_state)

	@property
	def TextBox160(self):
		self._getter_access_tracker["TextBox160"] = {}
		return self._TextBox160
	@TextBox160.setter
	def TextBox160(self, new_state):
		self._setter_access_tracker["TextBox160"] = {}
		self._TextBox160 = TextBox(new_state)

	@property
	def Flex180(self):
		self._getter_access_tracker["Flex180"] = {}
		return self._Flex180
	@Flex180.setter
	def Flex180(self, new_state):
		self._setter_access_tracker["Flex180"] = {}
		self._Flex180 = Flex(new_state)

	@property
	def Flex181(self):
		self._getter_access_tracker["Flex181"] = {}
		return self._Flex181
	@Flex181.setter
	def Flex181(self, new_state):
		self._setter_access_tracker["Flex181"] = {}
		self._Flex181 = Flex(new_state)

	@property
	def FramerText81(self):
		self._getter_access_tracker["FramerText81"] = {}
		return self._FramerText81
	@FramerText81.setter
	def FramerText81(self, new_state):
		self._setter_access_tracker["FramerText81"] = {}
		self._FramerText81 = FramerText(new_state)

	@property
	def FramerText82(self):
		self._getter_access_tracker["FramerText82"] = {}
		return self._FramerText82
	@FramerText82.setter
	def FramerText82(self, new_state):
		self._setter_access_tracker["FramerText82"] = {}
		self._FramerText82 = FramerText(new_state)

	@property
	def FramerText83(self):
		self._getter_access_tracker["FramerText83"] = {}
		return self._FramerText83
	@FramerText83.setter
	def FramerText83(self, new_state):
		self._setter_access_tracker["FramerText83"] = {}
		self._FramerText83 = FramerText(new_state)

	@property
	def FramerText84(self):
		self._getter_access_tracker["FramerText84"] = {}
		return self._FramerText84
	@FramerText84.setter
	def FramerText84(self, new_state):
		self._setter_access_tracker["FramerText84"] = {}
		self._FramerText84 = FramerText(new_state)

	@property
	def FramerText85(self):
		self._getter_access_tracker["FramerText85"] = {}
		return self._FramerText85
	@FramerText85.setter
	def FramerText85(self, new_state):
		self._setter_access_tracker["FramerText85"] = {}
		self._FramerText85 = FramerText(new_state)

	@property
	def FramerText86(self):
		self._getter_access_tracker["FramerText86"] = {}
		return self._FramerText86
	@FramerText86.setter
	def FramerText86(self, new_state):
		self._setter_access_tracker["FramerText86"] = {}
		self._FramerText86 = FramerText(new_state)

	@property
	def LineText5(self):
		self._getter_access_tracker["LineText5"] = {}
		return self._LineText5
	@LineText5.setter
	def LineText5(self, new_state):
		self._setter_access_tracker["LineText5"] = {}
		self._LineText5 = LineText(new_state)

	@property
	def FramerText87(self):
		self._getter_access_tracker["FramerText87"] = {}
		return self._FramerText87
	@FramerText87.setter
	def FramerText87(self, new_state):
		self._setter_access_tracker["FramerText87"] = {}
		self._FramerText87 = FramerText(new_state)

	@property
	def FramerText88(self):
		self._getter_access_tracker["FramerText88"] = {}
		return self._FramerText88
	@FramerText88.setter
	def FramerText88(self, new_state):
		self._setter_access_tracker["FramerText88"] = {}
		self._FramerText88 = FramerText(new_state)

	@property
	def FramerText89(self):
		self._getter_access_tracker["FramerText89"] = {}
		return self._FramerText89
	@FramerText89.setter
	def FramerText89(self, new_state):
		self._setter_access_tracker["FramerText89"] = {}
		self._FramerText89 = FramerText(new_state)

	@property
	def FramerText90(self):
		self._getter_access_tracker["FramerText90"] = {}
		return self._FramerText90
	@FramerText90.setter
	def FramerText90(self, new_state):
		self._setter_access_tracker["FramerText90"] = {}
		self._FramerText90 = FramerText(new_state)

	@property
	def FramerText91(self):
		self._getter_access_tracker["FramerText91"] = {}
		return self._FramerText91
	@FramerText91.setter
	def FramerText91(self, new_state):
		self._setter_access_tracker["FramerText91"] = {}
		self._FramerText91 = FramerText(new_state)

	@property
	def FramerText92(self):
		self._getter_access_tracker["FramerText92"] = {}
		return self._FramerText92
	@FramerText92.setter
	def FramerText92(self, new_state):
		self._setter_access_tracker["FramerText92"] = {}
		self._FramerText92 = FramerText(new_state)

	@property
	def FramerText93(self):
		self._getter_access_tracker["FramerText93"] = {}
		return self._FramerText93
	@FramerText93.setter
	def FramerText93(self, new_state):
		self._setter_access_tracker["FramerText93"] = {}
		self._FramerText93 = FramerText(new_state)

	@property
	def FramerText94(self):
		self._getter_access_tracker["FramerText94"] = {}
		return self._FramerText94
	@FramerText94.setter
	def FramerText94(self, new_state):
		self._setter_access_tracker["FramerText94"] = {}
		self._FramerText94 = FramerText(new_state)

	@property
	def FramerText95(self):
		self._getter_access_tracker["FramerText95"] = {}
		return self._FramerText95
	@FramerText95.setter
	def FramerText95(self, new_state):
		self._setter_access_tracker["FramerText95"] = {}
		self._FramerText95 = FramerText(new_state)

	@property
	def FramerText96(self):
		self._getter_access_tracker["FramerText96"] = {}
		return self._FramerText96
	@FramerText96.setter
	def FramerText96(self, new_state):
		self._setter_access_tracker["FramerText96"] = {}
		self._FramerText96 = FramerText(new_state)

	@property
	def FramerText97(self):
		self._getter_access_tracker["FramerText97"] = {}
		return self._FramerText97
	@FramerText97.setter
	def FramerText97(self, new_state):
		self._setter_access_tracker["FramerText97"] = {}
		self._FramerText97 = FramerText(new_state)

	@property
	def FramerText98(self):
		self._getter_access_tracker["FramerText98"] = {}
		return self._FramerText98
	@FramerText98.setter
	def FramerText98(self, new_state):
		self._setter_access_tracker["FramerText98"] = {}
		self._FramerText98 = FramerText(new_state)

	@property
	def FramerText99(self):
		self._getter_access_tracker["FramerText99"] = {}
		return self._FramerText99
	@FramerText99.setter
	def FramerText99(self, new_state):
		self._setter_access_tracker["FramerText99"] = {}
		self._FramerText99 = FramerText(new_state)

	@property
	def FramerText100(self):
		self._getter_access_tracker["FramerText100"] = {}
		return self._FramerText100
	@FramerText100.setter
	def FramerText100(self, new_state):
		self._setter_access_tracker["FramerText100"] = {}
		self._FramerText100 = FramerText(new_state)

	@property
	def FramerText101(self):
		self._getter_access_tracker["FramerText101"] = {}
		return self._FramerText101
	@FramerText101.setter
	def FramerText101(self, new_state):
		self._setter_access_tracker["FramerText101"] = {}
		self._FramerText101 = FramerText(new_state)

	@property
	def FramerText102(self):
		self._getter_access_tracker["FramerText102"] = {}
		return self._FramerText102
	@FramerText102.setter
	def FramerText102(self, new_state):
		self._setter_access_tracker["FramerText102"] = {}
		self._FramerText102 = FramerText(new_state)

	@property
	def FramerText103(self):
		self._getter_access_tracker["FramerText103"] = {}
		return self._FramerText103
	@FramerText103.setter
	def FramerText103(self, new_state):
		self._setter_access_tracker["FramerText103"] = {}
		self._FramerText103 = FramerText(new_state)

	@property
	def FramerText104(self):
		self._getter_access_tracker["FramerText104"] = {}
		return self._FramerText104
	@FramerText104.setter
	def FramerText104(self, new_state):
		self._setter_access_tracker["FramerText104"] = {}
		self._FramerText104 = FramerText(new_state)

	@property
	def FramerText105(self):
		self._getter_access_tracker["FramerText105"] = {}
		return self._FramerText105
	@FramerText105.setter
	def FramerText105(self, new_state):
		self._setter_access_tracker["FramerText105"] = {}
		self._FramerText105 = FramerText(new_state)

	@property
	def FramerText106(self):
		self._getter_access_tracker["FramerText106"] = {}
		return self._FramerText106
	@FramerText106.setter
	def FramerText106(self, new_state):
		self._setter_access_tracker["FramerText106"] = {}
		self._FramerText106 = FramerText(new_state)

	@property
	def FramerText107(self):
		self._getter_access_tracker["FramerText107"] = {}
		return self._FramerText107
	@FramerText107.setter
	def FramerText107(self, new_state):
		self._setter_access_tracker["FramerText107"] = {}
		self._FramerText107 = FramerText(new_state)

	@property
	def FramerText108(self):
		self._getter_access_tracker["FramerText108"] = {}
		return self._FramerText108
	@FramerText108.setter
	def FramerText108(self, new_state):
		self._setter_access_tracker["FramerText108"] = {}
		self._FramerText108 = FramerText(new_state)

	@property
	def FramerText109(self):
		self._getter_access_tracker["FramerText109"] = {}
		return self._FramerText109
	@FramerText109.setter
	def FramerText109(self, new_state):
		self._setter_access_tracker["FramerText109"] = {}
		self._FramerText109 = FramerText(new_state)

	@property
	def FramerText110(self):
		self._getter_access_tracker["FramerText110"] = {}
		return self._FramerText110
	@FramerText110.setter
	def FramerText110(self, new_state):
		self._setter_access_tracker["FramerText110"] = {}
		self._FramerText110 = FramerText(new_state)

	@property
	def FramerText111(self):
		self._getter_access_tracker["FramerText111"] = {}
		return self._FramerText111
	@FramerText111.setter
	def FramerText111(self, new_state):
		self._setter_access_tracker["FramerText111"] = {}
		self._FramerText111 = FramerText(new_state)

	@property
	def FramerText112(self):
		self._getter_access_tracker["FramerText112"] = {}
		return self._FramerText112
	@FramerText112.setter
	def FramerText112(self, new_state):
		self._setter_access_tracker["FramerText112"] = {}
		self._FramerText112 = FramerText(new_state)

	@property
	def FramerText113(self):
		self._getter_access_tracker["FramerText113"] = {}
		return self._FramerText113
	@FramerText113.setter
	def FramerText113(self, new_state):
		self._setter_access_tracker["FramerText113"] = {}
		self._FramerText113 = FramerText(new_state)

	@property
	def FramerText114(self):
		self._getter_access_tracker["FramerText114"] = {}
		return self._FramerText114
	@FramerText114.setter
	def FramerText114(self, new_state):
		self._setter_access_tracker["FramerText114"] = {}
		self._FramerText114 = FramerText(new_state)

	@property
	def FramerText115(self):
		self._getter_access_tracker["FramerText115"] = {}
		return self._FramerText115
	@FramerText115.setter
	def FramerText115(self, new_state):
		self._setter_access_tracker["FramerText115"] = {}
		self._FramerText115 = FramerText(new_state)

	@property
	def Anchor133(self):
		self._getter_access_tracker["Anchor133"] = {}
		return self._Anchor133
	@Anchor133.setter
	def Anchor133(self, new_state):
		self._setter_access_tracker["Anchor133"] = {}
		self._Anchor133 = Anchor(new_state)

	@property
	def Anchor134(self):
		self._getter_access_tracker["Anchor134"] = {}
		return self._Anchor134
	@Anchor134.setter
	def Anchor134(self, new_state):
		self._setter_access_tracker["Anchor134"] = {}
		self._Anchor134 = Anchor(new_state)

	@property
	def Anchor135(self):
		self._getter_access_tracker["Anchor135"] = {}
		return self._Anchor135
	@Anchor135.setter
	def Anchor135(self, new_state):
		self._setter_access_tracker["Anchor135"] = {}
		self._Anchor135 = Anchor(new_state)

	@property
	def Anchor136(self):
		self._getter_access_tracker["Anchor136"] = {}
		return self._Anchor136
	@Anchor136.setter
	def Anchor136(self, new_state):
		self._setter_access_tracker["Anchor136"] = {}
		self._Anchor136 = Anchor(new_state)

	@property
	def Anchor137(self):
		self._getter_access_tracker["Anchor137"] = {}
		return self._Anchor137
	@Anchor137.setter
	def Anchor137(self, new_state):
		self._setter_access_tracker["Anchor137"] = {}
		self._Anchor137 = Anchor(new_state)

	@property
	def Anchor138(self):
		self._getter_access_tracker["Anchor138"] = {}
		return self._Anchor138
	@Anchor138.setter
	def Anchor138(self, new_state):
		self._setter_access_tracker["Anchor138"] = {}
		self._Anchor138 = Anchor(new_state)

	@property
	def Anchor139(self):
		self._getter_access_tracker["Anchor139"] = {}
		return self._Anchor139
	@Anchor139.setter
	def Anchor139(self, new_state):
		self._setter_access_tracker["Anchor139"] = {}
		self._Anchor139 = Anchor(new_state)

	@property
	def Anchor140(self):
		self._getter_access_tracker["Anchor140"] = {}
		return self._Anchor140
	@Anchor140.setter
	def Anchor140(self, new_state):
		self._setter_access_tracker["Anchor140"] = {}
		self._Anchor140 = Anchor(new_state)

	@property
	def Anchor141(self):
		self._getter_access_tracker["Anchor141"] = {}
		return self._Anchor141
	@Anchor141.setter
	def Anchor141(self, new_state):
		self._setter_access_tracker["Anchor141"] = {}
		self._Anchor141 = Anchor(new_state)

	@property
	def Anchor142(self):
		self._getter_access_tracker["Anchor142"] = {}
		return self._Anchor142
	@Anchor142.setter
	def Anchor142(self, new_state):
		self._setter_access_tracker["Anchor142"] = {}
		self._Anchor142 = Anchor(new_state)

	@property
	def Anchor143(self):
		self._getter_access_tracker["Anchor143"] = {}
		return self._Anchor143
	@Anchor143.setter
	def Anchor143(self, new_state):
		self._setter_access_tracker["Anchor143"] = {}
		self._Anchor143 = Anchor(new_state)

	@property
	def Anchor144(self):
		self._getter_access_tracker["Anchor144"] = {}
		return self._Anchor144
	@Anchor144.setter
	def Anchor144(self, new_state):
		self._setter_access_tracker["Anchor144"] = {}
		self._Anchor144 = Anchor(new_state)

	@property
	def Anchor145(self):
		self._getter_access_tracker["Anchor145"] = {}
		return self._Anchor145
	@Anchor145.setter
	def Anchor145(self, new_state):
		self._setter_access_tracker["Anchor145"] = {}
		self._Anchor145 = Anchor(new_state)

	@property
	def Anchor146(self):
		self._getter_access_tracker["Anchor146"] = {}
		return self._Anchor146
	@Anchor146.setter
	def Anchor146(self, new_state):
		self._setter_access_tracker["Anchor146"] = {}
		self._Anchor146 = Anchor(new_state)

	@property
	def Anchor147(self):
		self._getter_access_tracker["Anchor147"] = {}
		return self._Anchor147
	@Anchor147.setter
	def Anchor147(self, new_state):
		self._setter_access_tracker["Anchor147"] = {}
		self._Anchor147 = Anchor(new_state)

	@property
	def Anchor148(self):
		self._getter_access_tracker["Anchor148"] = {}
		return self._Anchor148
	@Anchor148.setter
	def Anchor148(self, new_state):
		self._setter_access_tracker["Anchor148"] = {}
		self._Anchor148 = Anchor(new_state)

	@property
	def Anchor149(self):
		self._getter_access_tracker["Anchor149"] = {}
		return self._Anchor149
	@Anchor149.setter
	def Anchor149(self, new_state):
		self._setter_access_tracker["Anchor149"] = {}
		self._Anchor149 = Anchor(new_state)

	@property
	def Anchor150(self):
		self._getter_access_tracker["Anchor150"] = {}
		return self._Anchor150
	@Anchor150.setter
	def Anchor150(self, new_state):
		self._setter_access_tracker["Anchor150"] = {}
		self._Anchor150 = Anchor(new_state)

	@property
	def Anchor151(self):
		self._getter_access_tracker["Anchor151"] = {}
		return self._Anchor151
	@Anchor151.setter
	def Anchor151(self, new_state):
		self._setter_access_tracker["Anchor151"] = {}
		self._Anchor151 = Anchor(new_state)

	@property
	def Anchor152(self):
		self._getter_access_tracker["Anchor152"] = {}
		return self._Anchor152
	@Anchor152.setter
	def Anchor152(self, new_state):
		self._setter_access_tracker["Anchor152"] = {}
		self._Anchor152 = Anchor(new_state)

	@property
	def Anchor153(self):
		self._getter_access_tracker["Anchor153"] = {}
		return self._Anchor153
	@Anchor153.setter
	def Anchor153(self, new_state):
		self._setter_access_tracker["Anchor153"] = {}
		self._Anchor153 = Anchor(new_state)

	@property
	def Anchor154(self):
		self._getter_access_tracker["Anchor154"] = {}
		return self._Anchor154
	@Anchor154.setter
	def Anchor154(self, new_state):
		self._setter_access_tracker["Anchor154"] = {}
		self._Anchor154 = Anchor(new_state)

	@property
	def Anchor155(self):
		self._getter_access_tracker["Anchor155"] = {}
		return self._Anchor155
	@Anchor155.setter
	def Anchor155(self, new_state):
		self._setter_access_tracker["Anchor155"] = {}
		self._Anchor155 = Anchor(new_state)

	@property
	def Anchor156(self):
		self._getter_access_tracker["Anchor156"] = {}
		return self._Anchor156
	@Anchor156.setter
	def Anchor156(self, new_state):
		self._setter_access_tracker["Anchor156"] = {}
		self._Anchor156 = Anchor(new_state)

	@property
	def Anchor157(self):
		self._getter_access_tracker["Anchor157"] = {}
		return self._Anchor157
	@Anchor157.setter
	def Anchor157(self, new_state):
		self._setter_access_tracker["Anchor157"] = {}
		self._Anchor157 = Anchor(new_state)

	@property
	def Anchor158(self):
		self._getter_access_tracker["Anchor158"] = {}
		return self._Anchor158
	@Anchor158.setter
	def Anchor158(self, new_state):
		self._setter_access_tracker["Anchor158"] = {}
		self._Anchor158 = Anchor(new_state)

	@property
	def Anchor159(self):
		self._getter_access_tracker["Anchor159"] = {}
		return self._Anchor159
	@Anchor159.setter
	def Anchor159(self, new_state):
		self._setter_access_tracker["Anchor159"] = {}
		self._Anchor159 = Anchor(new_state)

	@property
	def Anchor160(self):
		self._getter_access_tracker["Anchor160"] = {}
		return self._Anchor160
	@Anchor160.setter
	def Anchor160(self, new_state):
		self._setter_access_tracker["Anchor160"] = {}
		self._Anchor160 = Anchor(new_state)

	@property
	def Anchor161(self):
		self._getter_access_tracker["Anchor161"] = {}
		return self._Anchor161
	@Anchor161.setter
	def Anchor161(self, new_state):
		self._setter_access_tracker["Anchor161"] = {}
		self._Anchor161 = Anchor(new_state)

	@property
	def Anchor162(self):
		self._getter_access_tracker["Anchor162"] = {}
		return self._Anchor162
	@Anchor162.setter
	def Anchor162(self, new_state):
		self._setter_access_tracker["Anchor162"] = {}
		self._Anchor162 = Anchor(new_state)

	@property
	def Anchor163(self):
		self._getter_access_tracker["Anchor163"] = {}
		return self._Anchor163
	@Anchor163.setter
	def Anchor163(self, new_state):
		self._setter_access_tracker["Anchor163"] = {}
		self._Anchor163 = Anchor(new_state)

	@property
	def Anchor164(self):
		self._getter_access_tracker["Anchor164"] = {}
		return self._Anchor164
	@Anchor164.setter
	def Anchor164(self, new_state):
		self._setter_access_tracker["Anchor164"] = {}
		self._Anchor164 = Anchor(new_state)

	@property
	def Anchor165(self):
		self._getter_access_tracker["Anchor165"] = {}
		return self._Anchor165
	@Anchor165.setter
	def Anchor165(self, new_state):
		self._setter_access_tracker["Anchor165"] = {}
		self._Anchor165 = Anchor(new_state)

	@property
	def Anchor166(self):
		self._getter_access_tracker["Anchor166"] = {}
		return self._Anchor166
	@Anchor166.setter
	def Anchor166(self, new_state):
		self._setter_access_tracker["Anchor166"] = {}
		self._Anchor166 = Anchor(new_state)

	@property
	def Anchor167(self):
		self._getter_access_tracker["Anchor167"] = {}
		return self._Anchor167
	@Anchor167.setter
	def Anchor167(self, new_state):
		self._setter_access_tracker["Anchor167"] = {}
		self._Anchor167 = Anchor(new_state)

	@property
	def Anchor168(self):
		self._getter_access_tracker["Anchor168"] = {}
		return self._Anchor168
	@Anchor168.setter
	def Anchor168(self, new_state):
		self._setter_access_tracker["Anchor168"] = {}
		self._Anchor168 = Anchor(new_state)

	@property
	def Flex182(self):
		self._getter_access_tracker["Flex182"] = {}
		return self._Flex182
	@Flex182.setter
	def Flex182(self, new_state):
		self._setter_access_tracker["Flex182"] = {}
		self._Flex182 = Flex(new_state)

	@property
	def TextBox161(self):
		self._getter_access_tracker["TextBox161"] = {}
		return self._TextBox161
	@TextBox161.setter
	def TextBox161(self, new_state):
		self._setter_access_tracker["TextBox161"] = {}
		self._TextBox161 = TextBox(new_state)

	@property
	def Flex183(self):
		self._getter_access_tracker["Flex183"] = {}
		return self._Flex183
	@Flex183.setter
	def Flex183(self, new_state):
		self._setter_access_tracker["Flex183"] = {}
		self._Flex183 = Flex(new_state)

	@property
	def TextBox162(self):
		self._getter_access_tracker["TextBox162"] = {}
		return self._TextBox162
	@TextBox162.setter
	def TextBox162(self, new_state):
		self._setter_access_tracker["TextBox162"] = {}
		self._TextBox162 = TextBox(new_state)

	@property
	def Flex184(self):
		self._getter_access_tracker["Flex184"] = {}
		return self._Flex184
	@Flex184.setter
	def Flex184(self, new_state):
		self._setter_access_tracker["Flex184"] = {}
		self._Flex184 = Flex(new_state)

	@property
	def Flex185(self):
		self._getter_access_tracker["Flex185"] = {}
		return self._Flex185
	@Flex185.setter
	def Flex185(self, new_state):
		self._setter_access_tracker["Flex185"] = {}
		self._Flex185 = Flex(new_state)

	@property
	def Flex186(self):
		self._getter_access_tracker["Flex186"] = {}
		return self._Flex186
	@Flex186.setter
	def Flex186(self, new_state):
		self._setter_access_tracker["Flex186"] = {}
		self._Flex186 = Flex(new_state)

	@property
	def Flex187(self):
		self._getter_access_tracker["Flex187"] = {}
		return self._Flex187
	@Flex187.setter
	def Flex187(self, new_state):
		self._setter_access_tracker["Flex187"] = {}
		self._Flex187 = Flex(new_state)

	@property
	def TextBox163(self):
		self._getter_access_tracker["TextBox163"] = {}
		return self._TextBox163
	@TextBox163.setter
	def TextBox163(self, new_state):
		self._setter_access_tracker["TextBox163"] = {}
		self._TextBox163 = TextBox(new_state)

	@property
	def Flex188(self):
		self._getter_access_tracker["Flex188"] = {}
		return self._Flex188
	@Flex188.setter
	def Flex188(self, new_state):
		self._setter_access_tracker["Flex188"] = {}
		self._Flex188 = Flex(new_state)

	@property
	def Flex189(self):
		self._getter_access_tracker["Flex189"] = {}
		return self._Flex189
	@Flex189.setter
	def Flex189(self, new_state):
		self._setter_access_tracker["Flex189"] = {}
		self._Flex189 = Flex(new_state)

	@property
	def Flex190(self):
		self._getter_access_tracker["Flex190"] = {}
		return self._Flex190
	@Flex190.setter
	def Flex190(self, new_state):
		self._setter_access_tracker["Flex190"] = {}
		self._Flex190 = Flex(new_state)

	@property
	def Flex191(self):
		self._getter_access_tracker["Flex191"] = {}
		return self._Flex191
	@Flex191.setter
	def Flex191(self, new_state):
		self._setter_access_tracker["Flex191"] = {}
		self._Flex191 = Flex(new_state)

	@property
	def Pages2(self):
		self._getter_access_tracker["Pages2"] = {}
		return self._Pages2
	@Pages2.setter
	def Pages2(self, new_state):
		self._setter_access_tracker["Pages2"] = {}
		self._Pages2 = Pages(new_state)
  
	def _to_json_fields(self):
		return {
			"ButtonFlex1": self._ButtonFlex1,
			"Flex1": self._Flex1,
			"Flex2": self._Flex2,
			"TextBox2": self._TextBox2,
			"ScaleFlex1": self._ScaleFlex1,
			"Image1": self._Image1,
			"Flex3": self._Flex3,
			"ButtonFlex2": self._ButtonFlex2,
			"TextBox3": self._TextBox3,
			"Anchor1": self._Anchor1,
			"Anchor2": self._Anchor2,
			"Anchor3": self._Anchor3,
			"Flex4": self._Flex4,
			"Flex5": self._Flex5,
			"FramerFlex1": self._FramerFlex1,
			"FramerFlex2": self._FramerFlex2,
			"Image2": self._Image2,
			"Flex6": self._Flex6,
			"Flex7": self._Flex7,
			"Flex8": self._Flex8,
			"TextBox4": self._TextBox4,
			"TextBox10": self._TextBox10,
			"ButtonFlex3": self._ButtonFlex3,
			"ButtonFlex4": self._ButtonFlex4,
			"TextBox11": self._TextBox11,
			"Anchor4": self._Anchor4,
			"Anchor5": self._Anchor5,
			"ScaleFlex2": self._ScaleFlex2,
			"TextBox14": self._TextBox14,
			"TextBox15": self._TextBox15,
			"TextBox16": self._TextBox16,
			"TextBox17": self._TextBox17,
			"TextBox18": self._TextBox18,
			"Anchor6": self._Anchor6,
			"Flex9": self._Flex9,
			"Anchor7": self._Anchor7,
			"FramerText1": self._FramerText1,
			"FramerText2": self._FramerText2,
			"Anchor8": self._Anchor8,
			"FramerText3": self._FramerText3,
			"Anchor9": self._Anchor9,
			"FramerText4": self._FramerText4,
			"Anchor10": self._Anchor10,
			"Pages1": self._Pages1,
			"Flex10": self._Flex10,
			"Flex11": self._Flex11,
			"DropdownMenu1": self._DropdownMenu1,
			"Flex12": self._Flex12,
			"Flex13": self._Flex13,
			"Flex14": self._Flex14,
			"TextBox19": self._TextBox19,
			"TextBox20": self._TextBox20,
			"TextBox21": self._TextBox21,
			"TextBox22": self._TextBox22,
			"TextBox23": self._TextBox23,
			"Flex15": self._Flex15,
			"Flex16": self._Flex16,
			"FramerText5": self._FramerText5,
			"Anchor11": self._Anchor11,
			"FramerText6": self._FramerText6,
			"Anchor12": self._Anchor12,
			"FramerText7": self._FramerText7,
			"Anchor13": self._Anchor13,
			"TextBox24": self._TextBox24,
			"TextBox25": self._TextBox25,
			"ButtonFlex5": self._ButtonFlex5,
			"Anchor14": self._Anchor14,
			"Flex17": self._Flex17,
			"TextBox28": self._TextBox28,
			"TextBox29": self._TextBox29,
			"ButtonFlex7": self._ButtonFlex7,
			"Anchor16": self._Anchor16,
			"Flex19": self._Flex19,
			"Flex20": self._Flex20,
			"FramerFlex3": self._FramerFlex3,
			"Image3": self._Image3,
			"Image4": self._Image4,
			"Image5": self._Image5,
			"Image6": self._Image6,
			"Image7": self._Image7,
			"Image8": self._Image8,
			"Flex21": self._Flex21,
			"Flex22": self._Flex22,
			"FramerFlex4": self._FramerFlex4,
			"Flex25": self._Flex25,
			"Div1": self._Div1,
			"TextBox30": self._TextBox30,
			"TextBox31": self._TextBox31,
			"TextBox32": self._TextBox32,
			"TextBox33": self._TextBox33,
			"TextBox34": self._TextBox34,
			"ButtonFlex8": self._ButtonFlex8,
			"ButtonFlex9": self._ButtonFlex9,
			"Anchor17": self._Anchor17,
			"Anchor18": self._Anchor18,
			"Flex26": self._Flex26,
			"FramerFlex7": self._FramerFlex7,
			"Flex32": self._Flex32,
			"Flex33": self._Flex33,
			"Flex35": self._Flex35,
			"Image9": self._Image9,
			"Div3": self._Div3,
			"Flex36": self._Flex36,
			"TextBox37": self._TextBox37,
			"TextBox38": self._TextBox38,
			"TextBox39": self._TextBox39,
			"Div4": self._Div4,
			"TextBox40": self._TextBox40,
			"TextBox41": self._TextBox41,
			"ButtonFlex12": self._ButtonFlex12,
			"Image10": self._Image10,
			"Anchor21": self._Anchor21,
			"FramerFlex8": self._FramerFlex8,
			"Flex37": self._Flex37,
			"Flex38": self._Flex38,
			"Flex39": self._Flex39,
			"Flex40": self._Flex40,
			"FramerFlex9": self._FramerFlex9,
			"Flex41": self._Flex41,
			"Flex42": self._Flex42,
			"Flex43": self._Flex43,
			"TextBox42": self._TextBox42,
			"TextBox43": self._TextBox43,
			"ButtonFlex13": self._ButtonFlex13,
			"Anchor22": self._Anchor22,
			"Div5": self._Div5,
			"TextBox44": self._TextBox44,
			"Flex44": self._Flex44,
			"Flex45": self._Flex45,
			"TextBox45": self._TextBox45,
			"TextBox46": self._TextBox46,
			"Div6": self._Div6,
			"Div7": self._Div7,
			"Image11": self._Image11,
			"Image12": self._Image12,
			"Image13": self._Image13,
			"Flex46": self._Flex46,
			"Flex47": self._Flex47,
			"FramerFlex10": self._FramerFlex10,
			"Image14": self._Image14,
			"Flex50": self._Flex50,
			"Flex51": self._Flex51,
			"Div8": self._Div8,
			"TextBox47": self._TextBox47,
			"Flex52": self._Flex52,
			"Flex53": self._Flex53,
			"Flex54": self._Flex54,
			"TextBox48": self._TextBox48,
			"TextBox49": self._TextBox49,
			"TextBox50": self._TextBox50,
			"TextBox51": self._TextBox51,
			"Flex55": self._Flex55,
			"TextBox52": self._TextBox52,
			"TextBox53": self._TextBox53,
			"Flex56": self._Flex56,
			"TextBox54": self._TextBox54,
			"TextBox55": self._TextBox55,
			"Flex57": self._Flex57,
			"Flex58": self._Flex58,
			"Flex59": self._Flex59,
			"FramerFlex11": self._FramerFlex11,
			"FramerFlex12": self._FramerFlex12,
			"Div9": self._Div9,
			"TextBox56": self._TextBox56,
			"Flex60": self._Flex60,
			"Flex61": self._Flex61,
			"Flex62": self._Flex62,
			"Flex63": self._Flex63,
			"TextBox57": self._TextBox57,
			"TextBox58": self._TextBox58,
			"TextBox59": self._TextBox59,
			"TextBox60": self._TextBox60,
			"TextBox61": self._TextBox61,
			"TextBox62": self._TextBox62,
			"TextBox63": self._TextBox63,
			"TextBox64": self._TextBox64,
			"Flex64": self._Flex64,
			"Flex65": self._Flex65,
			"Flex66": self._Flex66,
			"TextBox65": self._TextBox65,
			"TextBox66": self._TextBox66,
			"TextBox67": self._TextBox67,
			"TextBox68": self._TextBox68,
			"Flex67": self._Flex67,
			"Flex68": self._Flex68,
			"Flex69": self._Flex69,
			"Image15": self._Image15,
			"Flex70": self._Flex70,
			"ScaleFlex4": self._ScaleFlex4,
			"Image16": self._Image16,
			"Anchor23": self._Anchor23,
			"Flex71": self._Flex71,
			"Flex72": self._Flex72,
			"TextBox69": self._TextBox69,
			"TextBox70": self._TextBox70,
			"TextBox71": self._TextBox71,
			"TextBox72": self._TextBox72,
			"ButtonFlex14": self._ButtonFlex14,
			"ButtonFlex15": self._ButtonFlex15,
			"Anchor24": self._Anchor24,
			"Anchor25": self._Anchor25,
			"Flex73": self._Flex73,
			"Flex74": self._Flex74,
			"FramerFlex13": self._FramerFlex13,
			"FramerFlex14": self._FramerFlex14,
			"Flex75": self._Flex75,
			"TextBox73": self._TextBox73,
			"TextBox74": self._TextBox74,
			"ButtonFlex16": self._ButtonFlex16,
			"Anchor26": self._Anchor26,
			"Div11": self._Div11,
			"TextBox75": self._TextBox75,
			"Flex76": self._Flex76,
			"Flex78": self._Flex78,
			"TextBox76": self._TextBox76,
			"Accordion2": self._Accordion2,
			"Accordion3": self._Accordion3,
			"TextBox78": self._TextBox78,
			"Flex79": self._Flex79,
			"Flex80": self._Flex80,
			"Accordion4": self._Accordion4,
			"TextBox79": self._TextBox79,
			"Flex81": self._Flex81,
			"Flex82": self._Flex82,
			"Accordion5": self._Accordion5,
			"TextBox80": self._TextBox80,
			"Flex83": self._Flex83,
			"Flex84": self._Flex84,
			"Flex85": self._Flex85,
			"Flex86": self._Flex86,
			"FramerFlex15": self._FramerFlex15,
			"FramerFlex16": self._FramerFlex16,
			"Div12": self._Div12,
			"TextBox81": self._TextBox81,
			"Image26": self._Image26,
			"Flex103": self._Flex103,
			"TextBox94": self._TextBox94,
			"TextBox95": self._TextBox95,
			"Flex104": self._Flex104,
			"TextBox96": self._TextBox96,
			"Div17": self._Div17,
			"Image27": self._Image27,
			"Flex105": self._Flex105,
			"Flex106": self._Flex106,
			"ScaleFlex9": self._ScaleFlex9,
			"Image28": self._Image28,
			"TextBox97": self._TextBox97,
			"TextBox98": self._TextBox98,
			"Flex107": self._Flex107,
			"Image29": self._Image29,
			"Div18": self._Div18,
			"TextBox99": self._TextBox99,
			"Flex108": self._Flex108,
			"Flex109": self._Flex109,
			"Flex110": self._Flex110,
			"ScaleFlex10": self._ScaleFlex10,
			"Image30": self._Image30,
			"TextBox100": self._TextBox100,
			"TextBox101": self._TextBox101,
			"Flex111": self._Flex111,
			"Image31": self._Image31,
			"Div19": self._Div19,
			"TextBox102": self._TextBox102,
			"Flex112": self._Flex112,
			"Flex113": self._Flex113,
			"Flex114": self._Flex114,
			"ScaleFlex11": self._ScaleFlex11,
			"Anchor33": self._Anchor33,
			"Anchor34": self._Anchor34,
			"Anchor35": self._Anchor35,
			"Image32": self._Image32,
			"Flex115": self._Flex115,
			"TextBox103": self._TextBox103,
			"TextBox104": self._TextBox104,
			"Flex116": self._Flex116,
			"TextBox105": self._TextBox105,
			"Div20": self._Div20,
			"Image33": self._Image33,
			"Flex117": self._Flex117,
			"Flex118": self._Flex118,
			"ScaleFlex12": self._ScaleFlex12,
			"Anchor36": self._Anchor36,
			"Image34": self._Image34,
			"Flex119": self._Flex119,
			"TextBox106": self._TextBox106,
			"TextBox107": self._TextBox107,
			"Flex120": self._Flex120,
			"TextBox108": self._TextBox108,
			"Div21": self._Div21,
			"Image35": self._Image35,
			"Flex121": self._Flex121,
			"Flex122": self._Flex122,
			"ScaleFlex13": self._ScaleFlex13,
			"Anchor37": self._Anchor37,
			"Image36": self._Image36,
			"TextBox109": self._TextBox109,
			"TextBox110": self._TextBox110,
			"Flex123": self._Flex123,
			"Image37": self._Image37,
			"Div22": self._Div22,
			"TextBox111": self._TextBox111,
			"Flex124": self._Flex124,
			"Flex125": self._Flex125,
			"Flex126": self._Flex126,
			"ScaleFlex14": self._ScaleFlex14,
			"Anchor38": self._Anchor38,
			"Flex127": self._Flex127,
			"TextBox112": self._TextBox112,
			"TextBox117": self._TextBox117,
			"TextBox118": self._TextBox118,
			"TextBox119": self._TextBox119,
			"TextBox120": self._TextBox120,
			"ButtonFlex19": self._ButtonFlex19,
			"ButtonFlex20": self._ButtonFlex20,
			"Anchor41": self._Anchor41,
			"Anchor42": self._Anchor42,
			"Flex130": self._Flex130,
			"Flex131": self._Flex131,
			"Flex132": self._Flex132,
			"Flex133": self._Flex133,
			"FramerFlex17": self._FramerFlex17,
			"FramerFlex18": self._FramerFlex18,
			"Div23": self._Div23,
			"Flex134": self._Flex134,
			"Flex135": self._Flex135,
			"Flex136": self._Flex136,
			"Image38": self._Image38,
			"TextBox121": self._TextBox121,
			"Anchor43": self._Anchor43,
			"ScaleFlex15": self._ScaleFlex15,
			"Flex137": self._Flex137,
			"Flex138": self._Flex138,
			"Flex139": self._Flex139,
			"TextBox122": self._TextBox122,
			"Flex140": self._Flex140,
			"Anchor44": self._Anchor44,
			"FramerText8": self._FramerText8,
			"FramerText9": self._FramerText9,
			"Anchor45": self._Anchor45,
			"FramerText10": self._FramerText10,
			"Anchor46": self._Anchor46,
			"FramerText11": self._FramerText11,
			"Anchor47": self._Anchor47,
			"FramerText12": self._FramerText12,
			"Anchor48": self._Anchor48,
			"FramerText13": self._FramerText13,
			"Anchor49": self._Anchor49,
			"FramerText14": self._FramerText14,
			"FramerText15": self._FramerText15,
			"FramerText16": self._FramerText16,
			"FramerText17": self._FramerText17,
			"FramerText18": self._FramerText18,
			"FramerText19": self._FramerText19,
			"Anchor50": self._Anchor50,
			"Anchor51": self._Anchor51,
			"Anchor52": self._Anchor52,
			"Anchor53": self._Anchor53,
			"Anchor54": self._Anchor54,
			"Anchor55": self._Anchor55,
			"Flex141": self._Flex141,
			"TextBox123": self._TextBox123,
			"Flex142": self._Flex142,
			"FramerText20": self._FramerText20,
			"FramerText21": self._FramerText21,
			"FramerText22": self._FramerText22,
			"FramerText23": self._FramerText23,
			"FramerText24": self._FramerText24,
			"FramerText25": self._FramerText25,
			"Anchor56": self._Anchor56,
			"Anchor57": self._Anchor57,
			"Anchor58": self._Anchor58,
			"Anchor59": self._Anchor59,
			"Anchor60": self._Anchor60,
			"Anchor61": self._Anchor61,
			"Flex143": self._Flex143,
			"TextBox124": self._TextBox124,
			"Flex144": self._Flex144,
			"Flex145": self._Flex145,
			"FramerText26": self._FramerText26,
			"FramerText27": self._FramerText27,
			"FramerText28": self._FramerText28,
			"FramerText29": self._FramerText29,
			"FramerText30": self._FramerText30,
			"FramerText31": self._FramerText31,
			"Anchor62": self._Anchor62,
			"Anchor63": self._Anchor63,
			"Anchor64": self._Anchor64,
			"Anchor65": self._Anchor65,
			"Anchor66": self._Anchor66,
			"Anchor67": self._Anchor67,
			"Flex146": self._Flex146,
			"FramerText32": self._FramerText32,
			"Anchor68": self._Anchor68,
			"FramerText33": self._FramerText33,
			"Anchor69": self._Anchor69,
			"FramerText34": self._FramerText34,
			"Anchor70": self._Anchor70,
			"FramerText35": self._FramerText35,
			"Anchor71": self._Anchor71,
			"FramerText36": self._FramerText36,
			"Anchor72": self._Anchor72,
			"FramerText37": self._FramerText37,
			"Anchor73": self._Anchor73,
			"FramerText38": self._FramerText38,
			"Anchor74": self._Anchor74,
			"FramerText39": self._FramerText39,
			"Anchor75": self._Anchor75,
			"FramerText40": self._FramerText40,
			"Anchor76": self._Anchor76,
			"FramerText41": self._FramerText41,
			"Anchor77": self._Anchor77,
			"FramerText42": self._FramerText42,
			"Anchor78": self._Anchor78,
			"Flex147": self._Flex147,
			"TextBox125": self._TextBox125,
			"ButtonFlex21": self._ButtonFlex21,
			"Flex148": self._Flex148,
			"Anchor79": self._Anchor79,
			"Image39": self._Image39,
			"Image40": self._Image40,
			"ButtonFlex22": self._ButtonFlex22,
			"Anchor80": self._Anchor80,
			"Image41": self._Image41,
			"ButtonFlex23": self._ButtonFlex23,
			"Anchor81": self._Anchor81,
			"Image42": self._Image42,
			"ButtonFlex24": self._ButtonFlex24,
			"Anchor82": self._Anchor82,
			"Image43": self._Image43,
			"ButtonFlex25": self._ButtonFlex25,
			"Anchor83": self._Anchor83,
			"Image44": self._Image44,
			"ButtonFlex26": self._ButtonFlex26,
			"Anchor84": self._Anchor84,
			"Flex149": self._Flex149,
			"Div24": self._Div24,
			"Flex150": self._Flex150,
			"TextBox132": self._TextBox132,
			"Anchor85": self._Anchor85,
			"TextBox134": self._TextBox134,
			"FramerText43": self._FramerText43,
			"FramerText44": self._FramerText44,
			"Anchor87": self._Anchor87,
			"TextBox136": self._TextBox136,
			"Image45": self._Image45,
			"Anchor88": self._Anchor88,
			"TextBox137": self._TextBox137,
			"TextBox138": self._TextBox138,
			"TextBox139": self._TextBox139,
			"TextBox140": self._TextBox140,
			"TextBox141": self._TextBox141,
			"TextBox142": self._TextBox142,
			"LineText1": self._LineText1,
			"LineText2": self._LineText2,
			"Anchor89": self._Anchor89,
			"Anchor90": self._Anchor90,
			"ButtonFlex27": self._ButtonFlex27,
			"Flex151": self._Flex151,
			"Flex152": self._Flex152,
			"TextBox143": self._TextBox143,
			"Flex153": self._Flex153,
			"TextBox144": self._TextBox144,
			"TextBox145": self._TextBox145,
			"Flex154": self._Flex154,
			"Image46": self._Image46,
			"TextBox146": self._TextBox146,
			"TextBox147": self._TextBox147,
			"Image47": self._Image47,
			"Flex155": self._Flex155,
			"TextBox148": self._TextBox148,
			"Flex156": self._Flex156,
			"Flex157": self._Flex157,
			"Flex158": self._Flex158,
			"ButtonFlex28": self._ButtonFlex28,
			"Anchor91": self._Anchor91,
			"Flex159": self._Flex159,
			"FramerFlex19": self._FramerFlex19,
			"TextBox149": self._TextBox149,
			"TextBox150": self._TextBox150,
			"Image48": self._Image48,
			"Flex161": self._Flex161,
			"TextBox151": self._TextBox151,
			"Flex162": self._Flex162,
			"Flex163": self._Flex163,
			"Flex164": self._Flex164,
			"ButtonFlex29": self._ButtonFlex29,
			"Anchor92": self._Anchor92,
			"TextBox152": self._TextBox152,
			"TextBox153": self._TextBox153,
			"Image49": self._Image49,
			"Flex165": self._Flex165,
			"TextBox154": self._TextBox154,
			"Flex166": self._Flex166,
			"Flex167": self._Flex167,
			"Flex168": self._Flex168,
			"ButtonFlex30": self._ButtonFlex30,
			"Anchor93": self._Anchor93,
			"TextBox155": self._TextBox155,
			"TextBox156": self._TextBox156,
			"Image50": self._Image50,
			"Flex169": self._Flex169,
			"TextBox157": self._TextBox157,
			"Flex170": self._Flex170,
			"Flex171": self._Flex171,
			"Flex172": self._Flex172,
			"ButtonFlex31": self._ButtonFlex31,
			"Anchor94": self._Anchor94,
			"Anchor95": self._Anchor95,
			"LineText3": self._LineText3,
			"FramerFlex20": self._FramerFlex20,
			"FramerFlex21": self._FramerFlex21,
			"FramerText46": self._FramerText46,
			"FramerText47": self._FramerText47,
			"FramerText48": self._FramerText48,
			"FramerText49": self._FramerText49,
			"FramerText50": self._FramerText50,
			"FramerText51": self._FramerText51,
			"FramerText52": self._FramerText52,
			"FramerText53": self._FramerText53,
			"FramerText54": self._FramerText54,
			"FramerText55": self._FramerText55,
			"FramerText56": self._FramerText56,
			"FramerText57": self._FramerText57,
			"FramerText58": self._FramerText58,
			"FramerText59": self._FramerText59,
			"FramerText60": self._FramerText60,
			"FramerText61": self._FramerText61,
			"FramerText62": self._FramerText62,
			"FramerText63": self._FramerText63,
			"FramerText64": self._FramerText64,
			"FramerText65": self._FramerText65,
			"FramerText66": self._FramerText66,
			"FramerText67": self._FramerText67,
			"FramerText68": self._FramerText68,
			"Anchor97": self._Anchor97,
			"Anchor98": self._Anchor98,
			"Anchor99": self._Anchor99,
			"Anchor100": self._Anchor100,
			"Anchor101": self._Anchor101,
			"Anchor102": self._Anchor102,
			"Anchor103": self._Anchor103,
			"Anchor104": self._Anchor104,
			"Anchor105": self._Anchor105,
			"Anchor106": self._Anchor106,
			"Anchor107": self._Anchor107,
			"Anchor108": self._Anchor108,
			"Anchor109": self._Anchor109,
			"Anchor110": self._Anchor110,
			"Anchor111": self._Anchor111,
			"Anchor112": self._Anchor112,
			"Anchor113": self._Anchor113,
			"Anchor114": self._Anchor114,
			"Anchor115": self._Anchor115,
			"Anchor116": self._Anchor116,
			"Anchor117": self._Anchor117,
			"Anchor118": self._Anchor118,
			"Anchor119": self._Anchor119,
			"Flex173": self._Flex173,
			"Flex174": self._Flex174,
			"Flex175": self._Flex175,
			"TextBox158": self._TextBox158,
			"Flex176": self._Flex176,
			"FramerText69": self._FramerText69,
			"FramerText70": self._FramerText70,
			"FramerText71": self._FramerText71,
			"FramerText72": self._FramerText72,
			"FramerText73": self._FramerText73,
			"FramerText74": self._FramerText74,
			"Anchor120": self._Anchor120,
			"Anchor121": self._Anchor121,
			"Anchor122": self._Anchor122,
			"Anchor123": self._Anchor123,
			"Anchor124": self._Anchor124,
			"Anchor125": self._Anchor125,
			"TextBox159": self._TextBox159,
			"Flex177": self._Flex177,
			"Flex178": self._Flex178,
			"Flex179": self._Flex179,
			"LineText4": self._LineText4,
			"FramerText75": self._FramerText75,
			"FramerText76": self._FramerText76,
			"FramerText77": self._FramerText77,
			"FramerText78": self._FramerText78,
			"FramerText79": self._FramerText79,
			"FramerText80": self._FramerText80,
			"Anchor126": self._Anchor126,
			"Anchor127": self._Anchor127,
			"Anchor128": self._Anchor128,
			"Anchor129": self._Anchor129,
			"Anchor130": self._Anchor130,
			"Anchor131": self._Anchor131,
			"Anchor132": self._Anchor132,
			"TextBox160": self._TextBox160,
			"Flex180": self._Flex180,
			"Flex181": self._Flex181,
			"FramerText81": self._FramerText81,
			"FramerText82": self._FramerText82,
			"FramerText83": self._FramerText83,
			"FramerText84": self._FramerText84,
			"FramerText85": self._FramerText85,
			"FramerText86": self._FramerText86,
			"LineText5": self._LineText5,
			"FramerText87": self._FramerText87,
			"FramerText88": self._FramerText88,
			"FramerText89": self._FramerText89,
			"FramerText90": self._FramerText90,
			"FramerText91": self._FramerText91,
			"FramerText92": self._FramerText92,
			"FramerText93": self._FramerText93,
			"FramerText94": self._FramerText94,
			"FramerText95": self._FramerText95,
			"FramerText96": self._FramerText96,
			"FramerText97": self._FramerText97,
			"FramerText98": self._FramerText98,
			"FramerText99": self._FramerText99,
			"FramerText100": self._FramerText100,
			"FramerText101": self._FramerText101,
			"FramerText102": self._FramerText102,
			"FramerText103": self._FramerText103,
			"FramerText104": self._FramerText104,
			"FramerText105": self._FramerText105,
			"FramerText106": self._FramerText106,
			"FramerText107": self._FramerText107,
			"FramerText108": self._FramerText108,
			"FramerText109": self._FramerText109,
			"FramerText110": self._FramerText110,
			"FramerText111": self._FramerText111,
			"FramerText112": self._FramerText112,
			"FramerText113": self._FramerText113,
			"FramerText114": self._FramerText114,
			"FramerText115": self._FramerText115,
			"Anchor133": self._Anchor133,
			"Anchor134": self._Anchor134,
			"Anchor135": self._Anchor135,
			"Anchor136": self._Anchor136,
			"Anchor137": self._Anchor137,
			"Anchor138": self._Anchor138,
			"Anchor139": self._Anchor139,
			"Anchor140": self._Anchor140,
			"Anchor141": self._Anchor141,
			"Anchor142": self._Anchor142,
			"Anchor143": self._Anchor143,
			"Anchor144": self._Anchor144,
			"Anchor145": self._Anchor145,
			"Anchor146": self._Anchor146,
			"Anchor147": self._Anchor147,
			"Anchor148": self._Anchor148,
			"Anchor149": self._Anchor149,
			"Anchor150": self._Anchor150,
			"Anchor151": self._Anchor151,
			"Anchor152": self._Anchor152,
			"Anchor153": self._Anchor153,
			"Anchor154": self._Anchor154,
			"Anchor155": self._Anchor155,
			"Anchor156": self._Anchor156,
			"Anchor157": self._Anchor157,
			"Anchor158": self._Anchor158,
			"Anchor159": self._Anchor159,
			"Anchor160": self._Anchor160,
			"Anchor161": self._Anchor161,
			"Anchor162": self._Anchor162,
			"Anchor163": self._Anchor163,
			"Anchor164": self._Anchor164,
			"Anchor165": self._Anchor165,
			"Anchor166": self._Anchor166,
			"Anchor167": self._Anchor167,
			"Anchor168": self._Anchor168,
			"Flex182": self._Flex182,
			"TextBox161": self._TextBox161,
			"Flex183": self._Flex183,
			"TextBox162": self._TextBox162,
			"Flex184": self._Flex184,
			"Flex185": self._Flex185,
			"Flex186": self._Flex186,
			"Flex187": self._Flex187,
			"TextBox163": self._TextBox163,
			"Flex188": self._Flex188,
			"Flex189": self._Flex189,
			"Flex190": self._Flex190,
			"Flex191": self._Flex191,
			"Pages2": self._Pages2
			}
  