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
from manifests.FramerFlex import FramerFlex
from atri_react.Div import Div
from atri_react.Input import Input
from atri_react.Textarea import Textarea
from manifests.LineText import LineText
from atri_react.Accordion import Accordion


  
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
		self.Flex14 = state["Flex14"] if "Flex14" in state else None
		self.FramerFlex1 = state["FramerFlex1"] if "FramerFlex1" in state else None
		self.FramerFlex2 = state["FramerFlex2"] if "FramerFlex2" in state else None
		self.Flex15 = state["Flex15"] if "Flex15" in state else None
		self.Flex16 = state["Flex16"] if "Flex16" in state else None
		self.Flex17 = state["Flex17"] if "Flex17" in state else None
		self.Flex18 = state["Flex18"] if "Flex18" in state else None
		self.Div1 = state["Div1"] if "Div1" in state else None
		self.Flex19 = state["Flex19"] if "Flex19" in state else None
		self.TextBox9 = state["TextBox9"] if "TextBox9" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.Flex20 = state["Flex20"] if "Flex20" in state else None
		self.TextBox11 = state["TextBox11"] if "TextBox11" in state else None
		self.Anchor13 = state["Anchor13"] if "Anchor13" in state else None
		self.Anchor14 = state["Anchor14"] if "Anchor14" in state else None
		self.TextBox14 = state["TextBox14"] if "TextBox14" in state else None
		self.Flex21 = state["Flex21"] if "Flex21" in state else None
		self.Flex22 = state["Flex22"] if "Flex22" in state else None
		self.Input1 = state["Input1"] if "Input1" in state else None
		self.Input2 = state["Input2"] if "Input2" in state else None
		self.Flex23 = state["Flex23"] if "Flex23" in state else None
		self.Input3 = state["Input3"] if "Input3" in state else None
		self.Flex24 = state["Flex24"] if "Flex24" in state else None
		self.Flex25 = state["Flex25"] if "Flex25" in state else None
		self.Textarea1 = state["Textarea1"] if "Textarea1" in state else None
		self.ButtonFlex5 = state["ButtonFlex5"] if "ButtonFlex5" in state else None
		self.TextBox15 = state["TextBox15"] if "TextBox15" in state else None
		self.Anchor15 = state["Anchor15"] if "Anchor15" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.Anchor16 = state["Anchor16"] if "Anchor16" in state else None
		self.Image4 = state["Image4"] if "Image4" in state else None
		self.Anchor17 = state["Anchor17"] if "Anchor17" in state else None
		self.Image5 = state["Image5"] if "Image5" in state else None
		self.Anchor18 = state["Anchor18"] if "Anchor18" in state else None
		self.Image6 = state["Image6"] if "Image6" in state else None
		self.Anchor19 = state["Anchor19"] if "Anchor19" in state else None
		self.Image7 = state["Image7"] if "Image7" in state else None
		self.Anchor20 = state["Anchor20"] if "Anchor20" in state else None
		self.TextBox16 = state["TextBox16"] if "TextBox16" in state else None
		self.Image8 = state["Image8"] if "Image8" in state else None
		self.TextBox17 = state["TextBox17"] if "TextBox17" in state else None
		self.Image9 = state["Image9"] if "Image9" in state else None
		self.TextBox18 = state["TextBox18"] if "TextBox18" in state else None
		self.Image10 = state["Image10"] if "Image10" in state else None
		self.TextBox19 = state["TextBox19"] if "TextBox19" in state else None
		self.Image11 = state["Image11"] if "Image11" in state else None
		self.TextBox20 = state["TextBox20"] if "TextBox20" in state else None
		self.Image12 = state["Image12"] if "Image12" in state else None
		self.TextBox21 = state["TextBox21"] if "TextBox21" in state else None
		self.Image13 = state["Image13"] if "Image13" in state else None
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
		self.ButtonFlex6 = state["ButtonFlex6"] if "ButtonFlex6" in state else None
		self.ButtonFlex7 = state["ButtonFlex7"] if "ButtonFlex7" in state else None
		self.ButtonFlex8 = state["ButtonFlex8"] if "ButtonFlex8" in state else None
		self.ButtonFlex9 = state["ButtonFlex9"] if "ButtonFlex9" in state else None
		self.ButtonFlex10 = state["ButtonFlex10"] if "ButtonFlex10" in state else None
		self.ButtonFlex11 = state["ButtonFlex11"] if "ButtonFlex11" in state else None
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
		self.Anchor57 = state["Anchor57"] if "Anchor57" in state else None
		self.Anchor58 = state["Anchor58"] if "Anchor58" in state else None
		self.Anchor59 = state["Anchor59"] if "Anchor59" in state else None
		self.Anchor60 = state["Anchor60"] if "Anchor60" in state else None
		self.Anchor61 = state["Anchor61"] if "Anchor61" in state else None
		self.Anchor62 = state["Anchor62"] if "Anchor62" in state else None
		self.Flex26 = state["Flex26"] if "Flex26" in state else None
		self.Flex27 = state["Flex27"] if "Flex27" in state else None
		self.Image14 = state["Image14"] if "Image14" in state else None
		self.FramerText43 = state["FramerText43"] if "FramerText43" in state else None
		self.FramerText44 = state["FramerText44"] if "FramerText44" in state else None
		self.Flex28 = state["Flex28"] if "Flex28" in state else None
		self.TextBox22 = state["TextBox22"] if "TextBox22" in state else None
		self.TextBox23 = state["TextBox23"] if "TextBox23" in state else None
		self.Flex29 = state["Flex29"] if "Flex29" in state else None
		self.TextBox24 = state["TextBox24"] if "TextBox24" in state else None
		self.Flex30 = state["Flex30"] if "Flex30" in state else None
		self.Flex31 = state["Flex31"] if "Flex31" in state else None
		self.TextBox25 = state["TextBox25"] if "TextBox25" in state else None
		self.LineText2 = state["LineText2"] if "LineText2" in state else None
		self.LineText3 = state["LineText3"] if "LineText3" in state else None
		self.ScaleFlex2 = state["ScaleFlex2"] if "ScaleFlex2" in state else None
		self.Anchor63 = state["Anchor63"] if "Anchor63" in state else None
		self.TextBox26 = state["TextBox26"] if "TextBox26" in state else None
		self.Anchor64 = state["Anchor64"] if "Anchor64" in state else None
		self.TextBox27 = state["TextBox27"] if "TextBox27" in state else None
		self.Flex32 = state["Flex32"] if "Flex32" in state else None
		self.Flex33 = state["Flex33"] if "Flex33" in state else None
		self.Flex34 = state["Flex34"] if "Flex34" in state else None
		self.Flex35 = state["Flex35"] if "Flex35" in state else None
		self.Anchor65 = state["Anchor65"] if "Anchor65" in state else None
		self.Anchor66 = state["Anchor66"] if "Anchor66" in state else None
		self.Anchor67 = state["Anchor67"] if "Anchor67" in state else None
		self.TextBox28 = state["TextBox28"] if "TextBox28" in state else None
		self.Flex36 = state["Flex36"] if "Flex36" in state else None
		self.Div2 = state["Div2"] if "Div2" in state else None
		self.Flex37 = state["Flex37"] if "Flex37" in state else None
		self.Flex38 = state["Flex38"] if "Flex38" in state else None
		self.Flex39 = state["Flex39"] if "Flex39" in state else None
		self.Flex40 = state["Flex40"] if "Flex40" in state else None
		self.Flex41 = state["Flex41"] if "Flex41" in state else None
		self.Flex42 = state["Flex42"] if "Flex42" in state else None
		self.Div3 = state["Div3"] if "Div3" in state else None
		self.FramerFlex3 = state["FramerFlex3"] if "FramerFlex3" in state else None
		self.Flex43 = state["Flex43"] if "Flex43" in state else None
		self.footer1 = state["footer1"] if "footer1" in state else None
		self.TextBox29 = state["TextBox29"] if "TextBox29" in state else None
		self.Accordion1 = state["Accordion1"] if "Accordion1" in state else None
		self.TextBox30 = state["TextBox30"] if "TextBox30" in state else None
		self.Accordion2 = state["Accordion2"] if "Accordion2" in state else None
		self.TextBox31 = state["TextBox31"] if "TextBox31" in state else None
		self.Accordion3 = state["Accordion3"] if "Accordion3" in state else None
		self.Accordion4 = state["Accordion4"] if "Accordion4" in state else None
		self.TextBox32 = state["TextBox32"] if "TextBox32" in state else None
		self.TextBox33 = state["TextBox33"] if "TextBox33" in state else None
		self.TextBox34 = state["TextBox34"] if "TextBox34" in state else None
		self.Flex45 = state["Flex45"] if "Flex45" in state else None
		self.Flex46 = state["Flex46"] if "Flex46" in state else None
		self.Flex47 = state["Flex47"] if "Flex47" in state else None
		self.Flex48 = state["Flex48"] if "Flex48" in state else None
		self.ButtonFlex12 = state["ButtonFlex12"] if "ButtonFlex12" in state else None
		self.TextBox35 = state["TextBox35"] if "TextBox35" in state else None
		self.Div4 = state["Div4"] if "Div4" in state else None
		self.Flex49 = state["Flex49"] if "Flex49" in state else None
		self.Flex50 = state["Flex50"] if "Flex50" in state else None
		self.Flex51 = state["Flex51"] if "Flex51" in state else None
		self.Flex52 = state["Flex52"] if "Flex52" in state else None
		self.Anchor68 = state["Anchor68"] if "Anchor68" in state else None
		self.Flex53 = state["Flex53"] if "Flex53" in state else None
		self.FramerFlex4 = state["FramerFlex4"] if "FramerFlex4" in state else None
		self.FramerFlex5 = state["FramerFlex5"] if "FramerFlex5" in state else None
		self.Flex54 = state["Flex54"] if "Flex54" in state else None
		self.questions1 = state["questions1"] if "questions1" in state else None
		self.FramerText45 = state["FramerText45"] if "FramerText45" in state else None
		self.FramerText46 = state["FramerText46"] if "FramerText46" in state else None
		self.Flex56 = state["Flex56"] if "Flex56" in state else None
		self.Flex57 = state["Flex57"] if "Flex57" in state else None
		self.Flex58 = state["Flex58"] if "Flex58" in state else None
		self.Flex60 = state["Flex60"] if "Flex60" in state else None
		self.Accordion5 = state["Accordion5"] if "Accordion5" in state else None
		self.ButtonFlex13 = state["ButtonFlex13"] if "ButtonFlex13" in state else None
		self.TextBox36 = state["TextBox36"] if "TextBox36" in state else None
		self.TextBox37 = state["TextBox37"] if "TextBox37" in state else None
		self.Anchor69 = state["Anchor69"] if "Anchor69" in state else None
		self.TextBox38 = state["TextBox38"] if "TextBox38" in state else None
		self.TextBox39 = state["TextBox39"] if "TextBox39" in state else None
		self.ButtonFlex14 = state["ButtonFlex14"] if "ButtonFlex14" in state else None
		self.Anchor70 = state["Anchor70"] if "Anchor70" in state else None
		self.Accordion6 = state["Accordion6"] if "Accordion6" in state else None
		self.Flex62 = state["Flex62"] if "Flex62" in state else None
		self.TextBox40 = state["TextBox40"] if "TextBox40" in state else None
		self.TextBox41 = state["TextBox41"] if "TextBox41" in state else None
		self.ButtonFlex15 = state["ButtonFlex15"] if "ButtonFlex15" in state else None
		self.Anchor71 = state["Anchor71"] if "Anchor71" in state else None
		self.Accordion7 = state["Accordion7"] if "Accordion7" in state else None
		self.Flex63 = state["Flex63"] if "Flex63" in state else None
		self.Flex64 = state["Flex64"] if "Flex64" in state else None
		self.Image16 = state["Image16"] if "Image16" in state else None
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
	def Flex14(self):
		self._getter_access_tracker["Flex14"] = {}
		return self._Flex14
	@Flex14.setter
	def Flex14(self, new_state):
		self._setter_access_tracker["Flex14"] = {}
		self._Flex14 = Flex(new_state)

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
	def Flex17(self):
		self._getter_access_tracker["Flex17"] = {}
		return self._Flex17
	@Flex17.setter
	def Flex17(self, new_state):
		self._setter_access_tracker["Flex17"] = {}
		self._Flex17 = Flex(new_state)

	@property
	def Flex18(self):
		self._getter_access_tracker["Flex18"] = {}
		return self._Flex18
	@Flex18.setter
	def Flex18(self, new_state):
		self._setter_access_tracker["Flex18"] = {}
		self._Flex18 = Flex(new_state)

	@property
	def Div1(self):
		self._getter_access_tracker["Div1"] = {}
		return self._Div1
	@Div1.setter
	def Div1(self, new_state):
		self._setter_access_tracker["Div1"] = {}
		self._Div1 = Div(new_state)

	@property
	def Flex19(self):
		self._getter_access_tracker["Flex19"] = {}
		return self._Flex19
	@Flex19.setter
	def Flex19(self, new_state):
		self._setter_access_tracker["Flex19"] = {}
		self._Flex19 = Flex(new_state)

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
	def Flex20(self):
		self._getter_access_tracker["Flex20"] = {}
		return self._Flex20
	@Flex20.setter
	def Flex20(self, new_state):
		self._setter_access_tracker["Flex20"] = {}
		self._Flex20 = Flex(new_state)

	@property
	def TextBox11(self):
		self._getter_access_tracker["TextBox11"] = {}
		return self._TextBox11
	@TextBox11.setter
	def TextBox11(self, new_state):
		self._setter_access_tracker["TextBox11"] = {}
		self._TextBox11 = TextBox(new_state)

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
	def TextBox14(self):
		self._getter_access_tracker["TextBox14"] = {}
		return self._TextBox14
	@TextBox14.setter
	def TextBox14(self, new_state):
		self._setter_access_tracker["TextBox14"] = {}
		self._TextBox14 = TextBox(new_state)

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
	def Input1(self):
		self._getter_access_tracker["Input1"] = {}
		return self._Input1
	@Input1.setter
	def Input1(self, new_state):
		self._setter_access_tracker["Input1"] = {}
		self._Input1 = Input(new_state)

	@property
	def Input2(self):
		self._getter_access_tracker["Input2"] = {}
		return self._Input2
	@Input2.setter
	def Input2(self, new_state):
		self._setter_access_tracker["Input2"] = {}
		self._Input2 = Input(new_state)

	@property
	def Flex23(self):
		self._getter_access_tracker["Flex23"] = {}
		return self._Flex23
	@Flex23.setter
	def Flex23(self, new_state):
		self._setter_access_tracker["Flex23"] = {}
		self._Flex23 = Flex(new_state)

	@property
	def Input3(self):
		self._getter_access_tracker["Input3"] = {}
		return self._Input3
	@Input3.setter
	def Input3(self, new_state):
		self._setter_access_tracker["Input3"] = {}
		self._Input3 = Input(new_state)

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
	def Textarea1(self):
		self._getter_access_tracker["Textarea1"] = {}
		return self._Textarea1
	@Textarea1.setter
	def Textarea1(self, new_state):
		self._setter_access_tracker["Textarea1"] = {}
		self._Textarea1 = Textarea(new_state)

	@property
	def ButtonFlex5(self):
		self._getter_access_tracker["ButtonFlex5"] = {}
		return self._ButtonFlex5
	@ButtonFlex5.setter
	def ButtonFlex5(self, new_state):
		self._setter_access_tracker["ButtonFlex5"] = {}
		self._ButtonFlex5 = ButtonFlex(new_state)

	@property
	def TextBox15(self):
		self._getter_access_tracker["TextBox15"] = {}
		return self._TextBox15
	@TextBox15.setter
	def TextBox15(self, new_state):
		self._setter_access_tracker["TextBox15"] = {}
		self._TextBox15 = TextBox(new_state)

	@property
	def Anchor15(self):
		self._getter_access_tracker["Anchor15"] = {}
		return self._Anchor15
	@Anchor15.setter
	def Anchor15(self, new_state):
		self._setter_access_tracker["Anchor15"] = {}
		self._Anchor15 = Anchor(new_state)

	@property
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		self._Image3 = Image(new_state)

	@property
	def Anchor16(self):
		self._getter_access_tracker["Anchor16"] = {}
		return self._Anchor16
	@Anchor16.setter
	def Anchor16(self, new_state):
		self._setter_access_tracker["Anchor16"] = {}
		self._Anchor16 = Anchor(new_state)

	@property
	def Image4(self):
		self._getter_access_tracker["Image4"] = {}
		return self._Image4
	@Image4.setter
	def Image4(self, new_state):
		self._setter_access_tracker["Image4"] = {}
		self._Image4 = Image(new_state)

	@property
	def Anchor17(self):
		self._getter_access_tracker["Anchor17"] = {}
		return self._Anchor17
	@Anchor17.setter
	def Anchor17(self, new_state):
		self._setter_access_tracker["Anchor17"] = {}
		self._Anchor17 = Anchor(new_state)

	@property
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		self._Image5 = Image(new_state)

	@property
	def Anchor18(self):
		self._getter_access_tracker["Anchor18"] = {}
		return self._Anchor18
	@Anchor18.setter
	def Anchor18(self, new_state):
		self._setter_access_tracker["Anchor18"] = {}
		self._Anchor18 = Anchor(new_state)

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		self._Image6 = Image(new_state)

	@property
	def Anchor19(self):
		self._getter_access_tracker["Anchor19"] = {}
		return self._Anchor19
	@Anchor19.setter
	def Anchor19(self, new_state):
		self._setter_access_tracker["Anchor19"] = {}
		self._Anchor19 = Anchor(new_state)

	@property
	def Image7(self):
		self._getter_access_tracker["Image7"] = {}
		return self._Image7
	@Image7.setter
	def Image7(self, new_state):
		self._setter_access_tracker["Image7"] = {}
		self._Image7 = Image(new_state)

	@property
	def Anchor20(self):
		self._getter_access_tracker["Anchor20"] = {}
		return self._Anchor20
	@Anchor20.setter
	def Anchor20(self, new_state):
		self._setter_access_tracker["Anchor20"] = {}
		self._Anchor20 = Anchor(new_state)

	@property
	def TextBox16(self):
		self._getter_access_tracker["TextBox16"] = {}
		return self._TextBox16
	@TextBox16.setter
	def TextBox16(self, new_state):
		self._setter_access_tracker["TextBox16"] = {}
		self._TextBox16 = TextBox(new_state)

	@property
	def Image8(self):
		self._getter_access_tracker["Image8"] = {}
		return self._Image8
	@Image8.setter
	def Image8(self, new_state):
		self._setter_access_tracker["Image8"] = {}
		self._Image8 = Image(new_state)

	@property
	def TextBox17(self):
		self._getter_access_tracker["TextBox17"] = {}
		return self._TextBox17
	@TextBox17.setter
	def TextBox17(self, new_state):
		self._setter_access_tracker["TextBox17"] = {}
		self._TextBox17 = TextBox(new_state)

	@property
	def Image9(self):
		self._getter_access_tracker["Image9"] = {}
		return self._Image9
	@Image9.setter
	def Image9(self, new_state):
		self._setter_access_tracker["Image9"] = {}
		self._Image9 = Image(new_state)

	@property
	def TextBox18(self):
		self._getter_access_tracker["TextBox18"] = {}
		return self._TextBox18
	@TextBox18.setter
	def TextBox18(self, new_state):
		self._setter_access_tracker["TextBox18"] = {}
		self._TextBox18 = TextBox(new_state)

	@property
	def Image10(self):
		self._getter_access_tracker["Image10"] = {}
		return self._Image10
	@Image10.setter
	def Image10(self, new_state):
		self._setter_access_tracker["Image10"] = {}
		self._Image10 = Image(new_state)

	@property
	def TextBox19(self):
		self._getter_access_tracker["TextBox19"] = {}
		return self._TextBox19
	@TextBox19.setter
	def TextBox19(self, new_state):
		self._setter_access_tracker["TextBox19"] = {}
		self._TextBox19 = TextBox(new_state)

	@property
	def Image11(self):
		self._getter_access_tracker["Image11"] = {}
		return self._Image11
	@Image11.setter
	def Image11(self, new_state):
		self._setter_access_tracker["Image11"] = {}
		self._Image11 = Image(new_state)

	@property
	def TextBox20(self):
		self._getter_access_tracker["TextBox20"] = {}
		return self._TextBox20
	@TextBox20.setter
	def TextBox20(self, new_state):
		self._setter_access_tracker["TextBox20"] = {}
		self._TextBox20 = TextBox(new_state)

	@property
	def Image12(self):
		self._getter_access_tracker["Image12"] = {}
		return self._Image12
	@Image12.setter
	def Image12(self, new_state):
		self._setter_access_tracker["Image12"] = {}
		self._Image12 = Image(new_state)

	@property
	def TextBox21(self):
		self._getter_access_tracker["TextBox21"] = {}
		return self._TextBox21
	@TextBox21.setter
	def TextBox21(self, new_state):
		self._setter_access_tracker["TextBox21"] = {}
		self._TextBox21 = TextBox(new_state)

	@property
	def Image13(self):
		self._getter_access_tracker["Image13"] = {}
		return self._Image13
	@Image13.setter
	def Image13(self, new_state):
		self._setter_access_tracker["Image13"] = {}
		self._Image13 = Image(new_state)

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
	def ButtonFlex6(self):
		self._getter_access_tracker["ButtonFlex6"] = {}
		return self._ButtonFlex6
	@ButtonFlex6.setter
	def ButtonFlex6(self, new_state):
		self._setter_access_tracker["ButtonFlex6"] = {}
		self._ButtonFlex6 = ButtonFlex(new_state)

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
	def Anchor62(self):
		self._getter_access_tracker["Anchor62"] = {}
		return self._Anchor62
	@Anchor62.setter
	def Anchor62(self, new_state):
		self._setter_access_tracker["Anchor62"] = {}
		self._Anchor62 = Anchor(new_state)

	@property
	def Flex26(self):
		self._getter_access_tracker["Flex26"] = {}
		return self._Flex26
	@Flex26.setter
	def Flex26(self, new_state):
		self._setter_access_tracker["Flex26"] = {}
		self._Flex26 = Flex(new_state)

	@property
	def Flex27(self):
		self._getter_access_tracker["Flex27"] = {}
		return self._Flex27
	@Flex27.setter
	def Flex27(self, new_state):
		self._setter_access_tracker["Flex27"] = {}
		self._Flex27 = Flex(new_state)

	@property
	def Image14(self):
		self._getter_access_tracker["Image14"] = {}
		return self._Image14
	@Image14.setter
	def Image14(self, new_state):
		self._setter_access_tracker["Image14"] = {}
		self._Image14 = Image(new_state)

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
	def Flex28(self):
		self._getter_access_tracker["Flex28"] = {}
		return self._Flex28
	@Flex28.setter
	def Flex28(self, new_state):
		self._setter_access_tracker["Flex28"] = {}
		self._Flex28 = Flex(new_state)

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
	def Flex29(self):
		self._getter_access_tracker["Flex29"] = {}
		return self._Flex29
	@Flex29.setter
	def Flex29(self, new_state):
		self._setter_access_tracker["Flex29"] = {}
		self._Flex29 = Flex(new_state)

	@property
	def TextBox24(self):
		self._getter_access_tracker["TextBox24"] = {}
		return self._TextBox24
	@TextBox24.setter
	def TextBox24(self, new_state):
		self._setter_access_tracker["TextBox24"] = {}
		self._TextBox24 = TextBox(new_state)

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
	def TextBox25(self):
		self._getter_access_tracker["TextBox25"] = {}
		return self._TextBox25
	@TextBox25.setter
	def TextBox25(self, new_state):
		self._setter_access_tracker["TextBox25"] = {}
		self._TextBox25 = TextBox(new_state)

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
	def Anchor63(self):
		self._getter_access_tracker["Anchor63"] = {}
		return self._Anchor63
	@Anchor63.setter
	def Anchor63(self, new_state):
		self._setter_access_tracker["Anchor63"] = {}
		self._Anchor63 = Anchor(new_state)

	@property
	def TextBox26(self):
		self._getter_access_tracker["TextBox26"] = {}
		return self._TextBox26
	@TextBox26.setter
	def TextBox26(self, new_state):
		self._setter_access_tracker["TextBox26"] = {}
		self._TextBox26 = TextBox(new_state)

	@property
	def Anchor64(self):
		self._getter_access_tracker["Anchor64"] = {}
		return self._Anchor64
	@Anchor64.setter
	def Anchor64(self, new_state):
		self._setter_access_tracker["Anchor64"] = {}
		self._Anchor64 = Anchor(new_state)

	@property
	def TextBox27(self):
		self._getter_access_tracker["TextBox27"] = {}
		return self._TextBox27
	@TextBox27.setter
	def TextBox27(self, new_state):
		self._setter_access_tracker["TextBox27"] = {}
		self._TextBox27 = TextBox(new_state)

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
	def Flex34(self):
		self._getter_access_tracker["Flex34"] = {}
		return self._Flex34
	@Flex34.setter
	def Flex34(self, new_state):
		self._setter_access_tracker["Flex34"] = {}
		self._Flex34 = Flex(new_state)

	@property
	def Flex35(self):
		self._getter_access_tracker["Flex35"] = {}
		return self._Flex35
	@Flex35.setter
	def Flex35(self, new_state):
		self._setter_access_tracker["Flex35"] = {}
		self._Flex35 = Flex(new_state)

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
	def TextBox28(self):
		self._getter_access_tracker["TextBox28"] = {}
		return self._TextBox28
	@TextBox28.setter
	def TextBox28(self, new_state):
		self._setter_access_tracker["TextBox28"] = {}
		self._TextBox28 = TextBox(new_state)

	@property
	def Flex36(self):
		self._getter_access_tracker["Flex36"] = {}
		return self._Flex36
	@Flex36.setter
	def Flex36(self, new_state):
		self._setter_access_tracker["Flex36"] = {}
		self._Flex36 = Flex(new_state)

	@property
	def Div2(self):
		self._getter_access_tracker["Div2"] = {}
		return self._Div2
	@Div2.setter
	def Div2(self, new_state):
		self._setter_access_tracker["Div2"] = {}
		self._Div2 = Div(new_state)

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
	def Div3(self):
		self._getter_access_tracker["Div3"] = {}
		return self._Div3
	@Div3.setter
	def Div3(self, new_state):
		self._setter_access_tracker["Div3"] = {}
		self._Div3 = Div(new_state)

	@property
	def FramerFlex3(self):
		self._getter_access_tracker["FramerFlex3"] = {}
		return self._FramerFlex3
	@FramerFlex3.setter
	def FramerFlex3(self, new_state):
		self._setter_access_tracker["FramerFlex3"] = {}
		self._FramerFlex3 = FramerFlex(new_state)

	@property
	def Flex43(self):
		self._getter_access_tracker["Flex43"] = {}
		return self._Flex43
	@Flex43.setter
	def Flex43(self, new_state):
		self._setter_access_tracker["Flex43"] = {}
		self._Flex43 = Flex(new_state)

	@property
	def footer1(self):
		self._getter_access_tracker["footer1"] = {}
		return self._footer1
	@footer1.setter
	def footer1(self, new_state):
		self._setter_access_tracker["footer1"] = {}
		self._footer1 = Flex(new_state)

	@property
	def TextBox29(self):
		self._getter_access_tracker["TextBox29"] = {}
		return self._TextBox29
	@TextBox29.setter
	def TextBox29(self, new_state):
		self._setter_access_tracker["TextBox29"] = {}
		self._TextBox29 = TextBox(new_state)

	@property
	def Accordion1(self):
		self._getter_access_tracker["Accordion1"] = {}
		return self._Accordion1
	@Accordion1.setter
	def Accordion1(self, new_state):
		self._setter_access_tracker["Accordion1"] = {}
		self._Accordion1 = Accordion(new_state)

	@property
	def TextBox30(self):
		self._getter_access_tracker["TextBox30"] = {}
		return self._TextBox30
	@TextBox30.setter
	def TextBox30(self, new_state):
		self._setter_access_tracker["TextBox30"] = {}
		self._TextBox30 = TextBox(new_state)

	@property
	def Accordion2(self):
		self._getter_access_tracker["Accordion2"] = {}
		return self._Accordion2
	@Accordion2.setter
	def Accordion2(self, new_state):
		self._setter_access_tracker["Accordion2"] = {}
		self._Accordion2 = Accordion(new_state)

	@property
	def TextBox31(self):
		self._getter_access_tracker["TextBox31"] = {}
		return self._TextBox31
	@TextBox31.setter
	def TextBox31(self, new_state):
		self._setter_access_tracker["TextBox31"] = {}
		self._TextBox31 = TextBox(new_state)

	@property
	def Accordion3(self):
		self._getter_access_tracker["Accordion3"] = {}
		return self._Accordion3
	@Accordion3.setter
	def Accordion3(self, new_state):
		self._setter_access_tracker["Accordion3"] = {}
		self._Accordion3 = Accordion(new_state)

	@property
	def Accordion4(self):
		self._getter_access_tracker["Accordion4"] = {}
		return self._Accordion4
	@Accordion4.setter
	def Accordion4(self, new_state):
		self._setter_access_tracker["Accordion4"] = {}
		self._Accordion4 = Accordion(new_state)

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
	def Flex45(self):
		self._getter_access_tracker["Flex45"] = {}
		return self._Flex45
	@Flex45.setter
	def Flex45(self, new_state):
		self._setter_access_tracker["Flex45"] = {}
		self._Flex45 = Flex(new_state)

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
	def Flex48(self):
		self._getter_access_tracker["Flex48"] = {}
		return self._Flex48
	@Flex48.setter
	def Flex48(self, new_state):
		self._setter_access_tracker["Flex48"] = {}
		self._Flex48 = Flex(new_state)

	@property
	def ButtonFlex12(self):
		self._getter_access_tracker["ButtonFlex12"] = {}
		return self._ButtonFlex12
	@ButtonFlex12.setter
	def ButtonFlex12(self, new_state):
		self._setter_access_tracker["ButtonFlex12"] = {}
		self._ButtonFlex12 = ButtonFlex(new_state)

	@property
	def TextBox35(self):
		self._getter_access_tracker["TextBox35"] = {}
		return self._TextBox35
	@TextBox35.setter
	def TextBox35(self, new_state):
		self._setter_access_tracker["TextBox35"] = {}
		self._TextBox35 = TextBox(new_state)

	@property
	def Div4(self):
		self._getter_access_tracker["Div4"] = {}
		return self._Div4
	@Div4.setter
	def Div4(self, new_state):
		self._setter_access_tracker["Div4"] = {}
		self._Div4 = Div(new_state)

	@property
	def Flex49(self):
		self._getter_access_tracker["Flex49"] = {}
		return self._Flex49
	@Flex49.setter
	def Flex49(self, new_state):
		self._setter_access_tracker["Flex49"] = {}
		self._Flex49 = Flex(new_state)

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
	def Flex52(self):
		self._getter_access_tracker["Flex52"] = {}
		return self._Flex52
	@Flex52.setter
	def Flex52(self, new_state):
		self._setter_access_tracker["Flex52"] = {}
		self._Flex52 = Flex(new_state)

	@property
	def Anchor68(self):
		self._getter_access_tracker["Anchor68"] = {}
		return self._Anchor68
	@Anchor68.setter
	def Anchor68(self, new_state):
		self._setter_access_tracker["Anchor68"] = {}
		self._Anchor68 = Anchor(new_state)

	@property
	def Flex53(self):
		self._getter_access_tracker["Flex53"] = {}
		return self._Flex53
	@Flex53.setter
	def Flex53(self, new_state):
		self._setter_access_tracker["Flex53"] = {}
		self._Flex53 = Flex(new_state)

	@property
	def FramerFlex4(self):
		self._getter_access_tracker["FramerFlex4"] = {}
		return self._FramerFlex4
	@FramerFlex4.setter
	def FramerFlex4(self, new_state):
		self._setter_access_tracker["FramerFlex4"] = {}
		self._FramerFlex4 = FramerFlex(new_state)

	@property
	def FramerFlex5(self):
		self._getter_access_tracker["FramerFlex5"] = {}
		return self._FramerFlex5
	@FramerFlex5.setter
	def FramerFlex5(self, new_state):
		self._setter_access_tracker["FramerFlex5"] = {}
		self._FramerFlex5 = FramerFlex(new_state)

	@property
	def Flex54(self):
		self._getter_access_tracker["Flex54"] = {}
		return self._Flex54
	@Flex54.setter
	def Flex54(self, new_state):
		self._setter_access_tracker["Flex54"] = {}
		self._Flex54 = Flex(new_state)

	@property
	def questions1(self):
		self._getter_access_tracker["questions1"] = {}
		return self._questions1
	@questions1.setter
	def questions1(self, new_state):
		self._setter_access_tracker["questions1"] = {}
		self._questions1 = Flex(new_state)

	@property
	def FramerText45(self):
		self._getter_access_tracker["FramerText45"] = {}
		return self._FramerText45
	@FramerText45.setter
	def FramerText45(self, new_state):
		self._setter_access_tracker["FramerText45"] = {}
		self._FramerText45 = FramerText(new_state)

	@property
	def FramerText46(self):
		self._getter_access_tracker["FramerText46"] = {}
		return self._FramerText46
	@FramerText46.setter
	def FramerText46(self, new_state):
		self._setter_access_tracker["FramerText46"] = {}
		self._FramerText46 = FramerText(new_state)

	@property
	def Flex56(self):
		self._getter_access_tracker["Flex56"] = {}
		return self._Flex56
	@Flex56.setter
	def Flex56(self, new_state):
		self._setter_access_tracker["Flex56"] = {}
		self._Flex56 = Flex(new_state)

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
	def Flex60(self):
		self._getter_access_tracker["Flex60"] = {}
		return self._Flex60
	@Flex60.setter
	def Flex60(self, new_state):
		self._setter_access_tracker["Flex60"] = {}
		self._Flex60 = Flex(new_state)

	@property
	def Accordion5(self):
		self._getter_access_tracker["Accordion5"] = {}
		return self._Accordion5
	@Accordion5.setter
	def Accordion5(self, new_state):
		self._setter_access_tracker["Accordion5"] = {}
		self._Accordion5 = Accordion(new_state)

	@property
	def ButtonFlex13(self):
		self._getter_access_tracker["ButtonFlex13"] = {}
		return self._ButtonFlex13
	@ButtonFlex13.setter
	def ButtonFlex13(self, new_state):
		self._setter_access_tracker["ButtonFlex13"] = {}
		self._ButtonFlex13 = ButtonFlex(new_state)

	@property
	def TextBox36(self):
		self._getter_access_tracker["TextBox36"] = {}
		return self._TextBox36
	@TextBox36.setter
	def TextBox36(self, new_state):
		self._setter_access_tracker["TextBox36"] = {}
		self._TextBox36 = TextBox(new_state)

	@property
	def TextBox37(self):
		self._getter_access_tracker["TextBox37"] = {}
		return self._TextBox37
	@TextBox37.setter
	def TextBox37(self, new_state):
		self._setter_access_tracker["TextBox37"] = {}
		self._TextBox37 = TextBox(new_state)

	@property
	def Anchor69(self):
		self._getter_access_tracker["Anchor69"] = {}
		return self._Anchor69
	@Anchor69.setter
	def Anchor69(self, new_state):
		self._setter_access_tracker["Anchor69"] = {}
		self._Anchor69 = Anchor(new_state)

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
	def ButtonFlex14(self):
		self._getter_access_tracker["ButtonFlex14"] = {}
		return self._ButtonFlex14
	@ButtonFlex14.setter
	def ButtonFlex14(self, new_state):
		self._setter_access_tracker["ButtonFlex14"] = {}
		self._ButtonFlex14 = ButtonFlex(new_state)

	@property
	def Anchor70(self):
		self._getter_access_tracker["Anchor70"] = {}
		return self._Anchor70
	@Anchor70.setter
	def Anchor70(self, new_state):
		self._setter_access_tracker["Anchor70"] = {}
		self._Anchor70 = Anchor(new_state)

	@property
	def Accordion6(self):
		self._getter_access_tracker["Accordion6"] = {}
		return self._Accordion6
	@Accordion6.setter
	def Accordion6(self, new_state):
		self._setter_access_tracker["Accordion6"] = {}
		self._Accordion6 = Accordion(new_state)

	@property
	def Flex62(self):
		self._getter_access_tracker["Flex62"] = {}
		return self._Flex62
	@Flex62.setter
	def Flex62(self, new_state):
		self._setter_access_tracker["Flex62"] = {}
		self._Flex62 = Flex(new_state)

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
	def ButtonFlex15(self):
		self._getter_access_tracker["ButtonFlex15"] = {}
		return self._ButtonFlex15
	@ButtonFlex15.setter
	def ButtonFlex15(self, new_state):
		self._setter_access_tracker["ButtonFlex15"] = {}
		self._ButtonFlex15 = ButtonFlex(new_state)

	@property
	def Anchor71(self):
		self._getter_access_tracker["Anchor71"] = {}
		return self._Anchor71
	@Anchor71.setter
	def Anchor71(self, new_state):
		self._setter_access_tracker["Anchor71"] = {}
		self._Anchor71 = Anchor(new_state)

	@property
	def Accordion7(self):
		self._getter_access_tracker["Accordion7"] = {}
		return self._Accordion7
	@Accordion7.setter
	def Accordion7(self, new_state):
		self._setter_access_tracker["Accordion7"] = {}
		self._Accordion7 = Accordion(new_state)

	@property
	def Flex63(self):
		self._getter_access_tracker["Flex63"] = {}
		return self._Flex63
	@Flex63.setter
	def Flex63(self, new_state):
		self._setter_access_tracker["Flex63"] = {}
		self._Flex63 = Flex(new_state)

	@property
	def Flex64(self):
		self._getter_access_tracker["Flex64"] = {}
		return self._Flex64
	@Flex64.setter
	def Flex64(self, new_state):
		self._setter_access_tracker["Flex64"] = {}
		self._Flex64 = Flex(new_state)

	@property
	def Image16(self):
		self._getter_access_tracker["Image16"] = {}
		return self._Image16
	@Image16.setter
	def Image16(self, new_state):
		self._setter_access_tracker["Image16"] = {}
		self._Image16 = Image(new_state)
  
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
			"Flex14": self._Flex14,
			"FramerFlex1": self._FramerFlex1,
			"FramerFlex2": self._FramerFlex2,
			"Flex15": self._Flex15,
			"Flex16": self._Flex16,
			"Flex17": self._Flex17,
			"Flex18": self._Flex18,
			"Div1": self._Div1,
			"Flex19": self._Flex19,
			"TextBox9": self._TextBox9,
			"TextBox10": self._TextBox10,
			"Flex20": self._Flex20,
			"TextBox11": self._TextBox11,
			"Anchor13": self._Anchor13,
			"Anchor14": self._Anchor14,
			"TextBox14": self._TextBox14,
			"Flex21": self._Flex21,
			"Flex22": self._Flex22,
			"Input1": self._Input1,
			"Input2": self._Input2,
			"Flex23": self._Flex23,
			"Input3": self._Input3,
			"Flex24": self._Flex24,
			"Flex25": self._Flex25,
			"Textarea1": self._Textarea1,
			"ButtonFlex5": self._ButtonFlex5,
			"TextBox15": self._TextBox15,
			"Anchor15": self._Anchor15,
			"Image2": self._Image2,
			"Image3": self._Image3,
			"Anchor16": self._Anchor16,
			"Image4": self._Image4,
			"Anchor17": self._Anchor17,
			"Image5": self._Image5,
			"Anchor18": self._Anchor18,
			"Image6": self._Image6,
			"Anchor19": self._Anchor19,
			"Image7": self._Image7,
			"Anchor20": self._Anchor20,
			"TextBox16": self._TextBox16,
			"Image8": self._Image8,
			"TextBox17": self._TextBox17,
			"Image9": self._Image9,
			"TextBox18": self._TextBox18,
			"Image10": self._Image10,
			"TextBox19": self._TextBox19,
			"Image11": self._Image11,
			"TextBox20": self._TextBox20,
			"Image12": self._Image12,
			"TextBox21": self._TextBox21,
			"Image13": self._Image13,
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
			"ButtonFlex6": self._ButtonFlex6,
			"ButtonFlex7": self._ButtonFlex7,
			"ButtonFlex8": self._ButtonFlex8,
			"ButtonFlex9": self._ButtonFlex9,
			"ButtonFlex10": self._ButtonFlex10,
			"ButtonFlex11": self._ButtonFlex11,
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
			"Anchor57": self._Anchor57,
			"Anchor58": self._Anchor58,
			"Anchor59": self._Anchor59,
			"Anchor60": self._Anchor60,
			"Anchor61": self._Anchor61,
			"Anchor62": self._Anchor62,
			"Flex26": self._Flex26,
			"Flex27": self._Flex27,
			"Image14": self._Image14,
			"FramerText43": self._FramerText43,
			"FramerText44": self._FramerText44,
			"Flex28": self._Flex28,
			"TextBox22": self._TextBox22,
			"TextBox23": self._TextBox23,
			"Flex29": self._Flex29,
			"TextBox24": self._TextBox24,
			"Flex30": self._Flex30,
			"Flex31": self._Flex31,
			"TextBox25": self._TextBox25,
			"LineText2": self._LineText2,
			"LineText3": self._LineText3,
			"ScaleFlex2": self._ScaleFlex2,
			"Anchor63": self._Anchor63,
			"TextBox26": self._TextBox26,
			"Anchor64": self._Anchor64,
			"TextBox27": self._TextBox27,
			"Flex32": self._Flex32,
			"Flex33": self._Flex33,
			"Flex34": self._Flex34,
			"Flex35": self._Flex35,
			"Anchor65": self._Anchor65,
			"Anchor66": self._Anchor66,
			"Anchor67": self._Anchor67,
			"TextBox28": self._TextBox28,
			"Flex36": self._Flex36,
			"Div2": self._Div2,
			"Flex37": self._Flex37,
			"Flex38": self._Flex38,
			"Flex39": self._Flex39,
			"Flex40": self._Flex40,
			"Flex41": self._Flex41,
			"Flex42": self._Flex42,
			"Div3": self._Div3,
			"FramerFlex3": self._FramerFlex3,
			"Flex43": self._Flex43,
			"footer1": self._footer1,
			"TextBox29": self._TextBox29,
			"Accordion1": self._Accordion1,
			"TextBox30": self._TextBox30,
			"Accordion2": self._Accordion2,
			"TextBox31": self._TextBox31,
			"Accordion3": self._Accordion3,
			"Accordion4": self._Accordion4,
			"TextBox32": self._TextBox32,
			"TextBox33": self._TextBox33,
			"TextBox34": self._TextBox34,
			"Flex45": self._Flex45,
			"Flex46": self._Flex46,
			"Flex47": self._Flex47,
			"Flex48": self._Flex48,
			"ButtonFlex12": self._ButtonFlex12,
			"TextBox35": self._TextBox35,
			"Div4": self._Div4,
			"Flex49": self._Flex49,
			"Flex50": self._Flex50,
			"Flex51": self._Flex51,
			"Flex52": self._Flex52,
			"Anchor68": self._Anchor68,
			"Flex53": self._Flex53,
			"FramerFlex4": self._FramerFlex4,
			"FramerFlex5": self._FramerFlex5,
			"Flex54": self._Flex54,
			"questions1": self._questions1,
			"FramerText45": self._FramerText45,
			"FramerText46": self._FramerText46,
			"Flex56": self._Flex56,
			"Flex57": self._Flex57,
			"Flex58": self._Flex58,
			"Flex60": self._Flex60,
			"Accordion5": self._Accordion5,
			"ButtonFlex13": self._ButtonFlex13,
			"TextBox36": self._TextBox36,
			"TextBox37": self._TextBox37,
			"Anchor69": self._Anchor69,
			"TextBox38": self._TextBox38,
			"TextBox39": self._TextBox39,
			"ButtonFlex14": self._ButtonFlex14,
			"Anchor70": self._Anchor70,
			"Accordion6": self._Accordion6,
			"Flex62": self._Flex62,
			"TextBox40": self._TextBox40,
			"TextBox41": self._TextBox41,
			"ButtonFlex15": self._ButtonFlex15,
			"Anchor71": self._Anchor71,
			"Accordion7": self._Accordion7,
			"Flex63": self._Flex63,
			"Flex64": self._Flex64,
			"Image16": self._Image16
			}
  