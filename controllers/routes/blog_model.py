from typing import Union, Any
from atri_react.Flex import Flex
from manifests.FramerFlex import FramerFlex
from atri_react.TextBox import TextBox
from atri_react.Anchor import Anchor
from manifests.ScaleFlex import ScaleFlex
from atri_react.Image import Image
from atri_react.Div import Div
from manifests.ButtonFlex import ButtonFlex
from manifests.FramerText import FramerText
from atri_react.Input import Input


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.Flex1 = state["Flex1"] if "Flex1" in state else None
		self.Flex2 = state["Flex2"] if "Flex2" in state else None
		self.FramerFlex1 = state["FramerFlex1"] if "FramerFlex1" in state else None
		self.Flex3 = state["Flex3"] if "Flex3" in state else None
		self.TextBox1 = state["TextBox1"] if "TextBox1" in state else None
		self.FramerFlex3 = state["FramerFlex3"] if "FramerFlex3" in state else None
		self.Anchor1 = state["Anchor1"] if "Anchor1" in state else None
		self.ScaleFlex1 = state["ScaleFlex1"] if "ScaleFlex1" in state else None
		self.FramerFlex4 = state["FramerFlex4"] if "FramerFlex4" in state else None
		self.Flex4 = state["Flex4"] if "Flex4" in state else None
		self.Flex5 = state["Flex5"] if "Flex5" in state else None
		self.Image1 = state["Image1"] if "Image1" in state else None
		self.Flex6 = state["Flex6"] if "Flex6" in state else None
		self.TextBox4 = state["TextBox4"] if "TextBox4" in state else None
		self.TextBox5 = state["TextBox5"] if "TextBox5" in state else None
		self.Div1 = state["Div1"] if "Div1" in state else None
		self.TextBox6 = state["TextBox6"] if "TextBox6" in state else None
		self.ButtonFlex1 = state["ButtonFlex1"] if "ButtonFlex1" in state else None
		self.Div2 = state["Div2"] if "Div2" in state else None
		self.Flex8 = state["Flex8"] if "Flex8" in state else None
		self.TextBox9 = state["TextBox9"] if "TextBox9" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.Anchor2 = state["Anchor2"] if "Anchor2" in state else None
		self.TextBox12 = state["TextBox12"] if "TextBox12" in state else None
		self.TextBox13 = state["TextBox13"] if "TextBox13" in state else None
		self.Div3 = state["Div3"] if "Div3" in state else None
		self.Flex9 = state["Flex9"] if "Flex9" in state else None
		self.ButtonFlex2 = state["ButtonFlex2"] if "ButtonFlex2" in state else None
		self.Anchor3 = state["Anchor3"] if "Anchor3" in state else None
		self.TextBox15 = state["TextBox15"] if "TextBox15" in state else None
		self.TextBox16 = state["TextBox16"] if "TextBox16" in state else None
		self.Div4 = state["Div4"] if "Div4" in state else None
		self.Flex10 = state["Flex10"] if "Flex10" in state else None
		self.ButtonFlex3 = state["ButtonFlex3"] if "ButtonFlex3" in state else None
		self.Anchor4 = state["Anchor4"] if "Anchor4" in state else None
		self.Div5 = state["Div5"] if "Div5" in state else None
		self.Div6 = state["Div6"] if "Div6" in state else None
		self.Div7 = state["Div7"] if "Div7" in state else None
		self.TextBox18 = state["TextBox18"] if "TextBox18" in state else None
		self.TextBox19 = state["TextBox19"] if "TextBox19" in state else None
		self.TextBox20 = state["TextBox20"] if "TextBox20" in state else None
		self.Flex11 = state["Flex11"] if "Flex11" in state else None
		self.Flex12 = state["Flex12"] if "Flex12" in state else None
		self.FramerFlex5 = state["FramerFlex5"] if "FramerFlex5" in state else None
		self.Flex13 = state["Flex13"] if "Flex13" in state else None
		self.Flex14 = state["Flex14"] if "Flex14" in state else None
		self.TextBox21 = state["TextBox21"] if "TextBox21" in state else None
		self.FramerText1 = state["FramerText1"] if "FramerText1" in state else None
		self.Anchor6 = state["Anchor6"] if "Anchor6" in state else None
		self.Anchor7 = state["Anchor7"] if "Anchor7" in state else None
		self.FramerText2 = state["FramerText2"] if "FramerText2" in state else None
		self.FramerText3 = state["FramerText3"] if "FramerText3" in state else None
		self.Anchor8 = state["Anchor8"] if "Anchor8" in state else None
		self.FramerText4 = state["FramerText4"] if "FramerText4" in state else None
		self.Anchor9 = state["Anchor9"] if "Anchor9" in state else None
		self.Flex15 = state["Flex15"] if "Flex15" in state else None
		self.Flex16 = state["Flex16"] if "Flex16" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.Flex17 = state["Flex17"] if "Flex17" in state else None
		self.TextBox22 = state["TextBox22"] if "TextBox22" in state else None
		self.TextBox23 = state["TextBox23"] if "TextBox23" in state else None
		self.Flex18 = state["Flex18"] if "Flex18" in state else None
		self.TextBox24 = state["TextBox24"] if "TextBox24" in state else None
		self.Div8 = state["Div8"] if "Div8" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.Flex19 = state["Flex19"] if "Flex19" in state else None
		self.Flex20 = state["Flex20"] if "Flex20" in state else None
		self.ScaleFlex2 = state["ScaleFlex2"] if "ScaleFlex2" in state else None
		self.article1 = state["article1"] if "article1" in state else None
		self.FramerFlex6 = state["FramerFlex6"] if "FramerFlex6" in state else None
		self.Image8 = state["Image8"] if "Image8" in state else None
		self.TextBox31 = state["TextBox31"] if "TextBox31" in state else None
		self.TextBox32 = state["TextBox32"] if "TextBox32" in state else None
		self.Flex29 = state["Flex29"] if "Flex29" in state else None
		self.Image9 = state["Image9"] if "Image9" in state else None
		self.Div11 = state["Div11"] if "Div11" in state else None
		self.TextBox33 = state["TextBox33"] if "TextBox33" in state else None
		self.Flex30 = state["Flex30"] if "Flex30" in state else None
		self.Flex31 = state["Flex31"] if "Flex31" in state else None
		self.Flex32 = state["Flex32"] if "Flex32" in state else None
		self.ScaleFlex5 = state["ScaleFlex5"] if "ScaleFlex5" in state else None
		self.Anchor13 = state["Anchor13"] if "Anchor13" in state else None
		self.FramerFlex9 = state["FramerFlex9"] if "FramerFlex9" in state else None
		self.Image10 = state["Image10"] if "Image10" in state else None
		self.TextBox34 = state["TextBox34"] if "TextBox34" in state else None
		self.TextBox35 = state["TextBox35"] if "TextBox35" in state else None
		self.Flex33 = state["Flex33"] if "Flex33" in state else None
		self.Image11 = state["Image11"] if "Image11" in state else None
		self.Div12 = state["Div12"] if "Div12" in state else None
		self.TextBox36 = state["TextBox36"] if "TextBox36" in state else None
		self.Flex34 = state["Flex34"] if "Flex34" in state else None
		self.Flex35 = state["Flex35"] if "Flex35" in state else None
		self.Flex36 = state["Flex36"] if "Flex36" in state else None
		self.ScaleFlex6 = state["ScaleFlex6"] if "ScaleFlex6" in state else None
		self.Anchor14 = state["Anchor14"] if "Anchor14" in state else None
		self.FramerFlex10 = state["FramerFlex10"] if "FramerFlex10" in state else None
		self.Image12 = state["Image12"] if "Image12" in state else None
		self.TextBox37 = state["TextBox37"] if "TextBox37" in state else None
		self.TextBox38 = state["TextBox38"] if "TextBox38" in state else None
		self.Flex37 = state["Flex37"] if "Flex37" in state else None
		self.Image13 = state["Image13"] if "Image13" in state else None
		self.Div13 = state["Div13"] if "Div13" in state else None
		self.TextBox39 = state["TextBox39"] if "TextBox39" in state else None
		self.Flex38 = state["Flex38"] if "Flex38" in state else None
		self.Flex39 = state["Flex39"] if "Flex39" in state else None
		self.Flex40 = state["Flex40"] if "Flex40" in state else None
		self.ScaleFlex7 = state["ScaleFlex7"] if "ScaleFlex7" in state else None
		self.Anchor15 = state["Anchor15"] if "Anchor15" in state else None
		self.FramerFlex11 = state["FramerFlex11"] if "FramerFlex11" in state else None
		self.Image14 = state["Image14"] if "Image14" in state else None
		self.TextBox40 = state["TextBox40"] if "TextBox40" in state else None
		self.TextBox41 = state["TextBox41"] if "TextBox41" in state else None
		self.Flex41 = state["Flex41"] if "Flex41" in state else None
		self.Image15 = state["Image15"] if "Image15" in state else None
		self.Div14 = state["Div14"] if "Div14" in state else None
		self.TextBox42 = state["TextBox42"] if "TextBox42" in state else None
		self.Flex42 = state["Flex42"] if "Flex42" in state else None
		self.Flex43 = state["Flex43"] if "Flex43" in state else None
		self.Flex44 = state["Flex44"] if "Flex44" in state else None
		self.ScaleFlex8 = state["ScaleFlex8"] if "ScaleFlex8" in state else None
		self.Anchor16 = state["Anchor16"] if "Anchor16" in state else None
		self.FramerFlex12 = state["FramerFlex12"] if "FramerFlex12" in state else None
		self.Image16 = state["Image16"] if "Image16" in state else None
		self.TextBox43 = state["TextBox43"] if "TextBox43" in state else None
		self.TextBox44 = state["TextBox44"] if "TextBox44" in state else None
		self.Flex45 = state["Flex45"] if "Flex45" in state else None
		self.Image17 = state["Image17"] if "Image17" in state else None
		self.Div15 = state["Div15"] if "Div15" in state else None
		self.TextBox45 = state["TextBox45"] if "TextBox45" in state else None
		self.Flex46 = state["Flex46"] if "Flex46" in state else None
		self.Flex47 = state["Flex47"] if "Flex47" in state else None
		self.Flex48 = state["Flex48"] if "Flex48" in state else None
		self.ScaleFlex9 = state["ScaleFlex9"] if "ScaleFlex9" in state else None
		self.Anchor17 = state["Anchor17"] if "Anchor17" in state else None
		self.FramerFlex13 = state["FramerFlex13"] if "FramerFlex13" in state else None
		self.Flex49 = state["Flex49"] if "Flex49" in state else None
		self.Flex50 = state["Flex50"] if "Flex50" in state else None
		self.FramerFlex14 = state["FramerFlex14"] if "FramerFlex14" in state else None
		self.TextBox46 = state["TextBox46"] if "TextBox46" in state else None
		self.Input1 = state["Input1"] if "Input1" in state else None
		self.ButtonFlex4 = state["ButtonFlex4"] if "ButtonFlex4" in state else None
		self.FramerText5 = state["FramerText5"] if "FramerText5" in state else None
		self.Flex52 = state["Flex52"] if "Flex52" in state else None
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
	def FramerFlex1(self):
		self._getter_access_tracker["FramerFlex1"] = {}
		return self._FramerFlex1
	@FramerFlex1.setter
	def FramerFlex1(self, new_state):
		self._setter_access_tracker["FramerFlex1"] = {}
		self._FramerFlex1 = FramerFlex(new_state)

	@property
	def Flex3(self):
		self._getter_access_tracker["Flex3"] = {}
		return self._Flex3
	@Flex3.setter
	def Flex3(self, new_state):
		self._setter_access_tracker["Flex3"] = {}
		self._Flex3 = Flex(new_state)

	@property
	def TextBox1(self):
		self._getter_access_tracker["TextBox1"] = {}
		return self._TextBox1
	@TextBox1.setter
	def TextBox1(self, new_state):
		self._setter_access_tracker["TextBox1"] = {}
		self._TextBox1 = TextBox(new_state)

	@property
	def FramerFlex3(self):
		self._getter_access_tracker["FramerFlex3"] = {}
		return self._FramerFlex3
	@FramerFlex3.setter
	def FramerFlex3(self, new_state):
		self._setter_access_tracker["FramerFlex3"] = {}
		self._FramerFlex3 = FramerFlex(new_state)

	@property
	def Anchor1(self):
		self._getter_access_tracker["Anchor1"] = {}
		return self._Anchor1
	@Anchor1.setter
	def Anchor1(self, new_state):
		self._setter_access_tracker["Anchor1"] = {}
		self._Anchor1 = Anchor(new_state)

	@property
	def ScaleFlex1(self):
		self._getter_access_tracker["ScaleFlex1"] = {}
		return self._ScaleFlex1
	@ScaleFlex1.setter
	def ScaleFlex1(self, new_state):
		self._setter_access_tracker["ScaleFlex1"] = {}
		self._ScaleFlex1 = ScaleFlex(new_state)

	@property
	def FramerFlex4(self):
		self._getter_access_tracker["FramerFlex4"] = {}
		return self._FramerFlex4
	@FramerFlex4.setter
	def FramerFlex4(self, new_state):
		self._setter_access_tracker["FramerFlex4"] = {}
		self._FramerFlex4 = FramerFlex(new_state)

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
	def Image1(self):
		self._getter_access_tracker["Image1"] = {}
		return self._Image1
	@Image1.setter
	def Image1(self, new_state):
		self._setter_access_tracker["Image1"] = {}
		self._Image1 = Image(new_state)

	@property
	def Flex6(self):
		self._getter_access_tracker["Flex6"] = {}
		return self._Flex6
	@Flex6.setter
	def Flex6(self, new_state):
		self._setter_access_tracker["Flex6"] = {}
		self._Flex6 = Flex(new_state)

	@property
	def TextBox4(self):
		self._getter_access_tracker["TextBox4"] = {}
		return self._TextBox4
	@TextBox4.setter
	def TextBox4(self, new_state):
		self._setter_access_tracker["TextBox4"] = {}
		self._TextBox4 = TextBox(new_state)

	@property
	def TextBox5(self):
		self._getter_access_tracker["TextBox5"] = {}
		return self._TextBox5
	@TextBox5.setter
	def TextBox5(self, new_state):
		self._setter_access_tracker["TextBox5"] = {}
		self._TextBox5 = TextBox(new_state)

	@property
	def Div1(self):
		self._getter_access_tracker["Div1"] = {}
		return self._Div1
	@Div1.setter
	def Div1(self, new_state):
		self._setter_access_tracker["Div1"] = {}
		self._Div1 = Div(new_state)

	@property
	def TextBox6(self):
		self._getter_access_tracker["TextBox6"] = {}
		return self._TextBox6
	@TextBox6.setter
	def TextBox6(self, new_state):
		self._setter_access_tracker["TextBox6"] = {}
		self._TextBox6 = TextBox(new_state)

	@property
	def ButtonFlex1(self):
		self._getter_access_tracker["ButtonFlex1"] = {}
		return self._ButtonFlex1
	@ButtonFlex1.setter
	def ButtonFlex1(self, new_state):
		self._setter_access_tracker["ButtonFlex1"] = {}
		self._ButtonFlex1 = ButtonFlex(new_state)

	@property
	def Div2(self):
		self._getter_access_tracker["Div2"] = {}
		return self._Div2
	@Div2.setter
	def Div2(self, new_state):
		self._setter_access_tracker["Div2"] = {}
		self._Div2 = Div(new_state)

	@property
	def Flex8(self):
		self._getter_access_tracker["Flex8"] = {}
		return self._Flex8
	@Flex8.setter
	def Flex8(self, new_state):
		self._setter_access_tracker["Flex8"] = {}
		self._Flex8 = Flex(new_state)

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
	def Anchor2(self):
		self._getter_access_tracker["Anchor2"] = {}
		return self._Anchor2
	@Anchor2.setter
	def Anchor2(self, new_state):
		self._setter_access_tracker["Anchor2"] = {}
		self._Anchor2 = Anchor(new_state)

	@property
	def TextBox12(self):
		self._getter_access_tracker["TextBox12"] = {}
		return self._TextBox12
	@TextBox12.setter
	def TextBox12(self, new_state):
		self._setter_access_tracker["TextBox12"] = {}
		self._TextBox12 = TextBox(new_state)

	@property
	def TextBox13(self):
		self._getter_access_tracker["TextBox13"] = {}
		return self._TextBox13
	@TextBox13.setter
	def TextBox13(self, new_state):
		self._setter_access_tracker["TextBox13"] = {}
		self._TextBox13 = TextBox(new_state)

	@property
	def Div3(self):
		self._getter_access_tracker["Div3"] = {}
		return self._Div3
	@Div3.setter
	def Div3(self, new_state):
		self._setter_access_tracker["Div3"] = {}
		self._Div3 = Div(new_state)

	@property
	def Flex9(self):
		self._getter_access_tracker["Flex9"] = {}
		return self._Flex9
	@Flex9.setter
	def Flex9(self, new_state):
		self._setter_access_tracker["Flex9"] = {}
		self._Flex9 = Flex(new_state)

	@property
	def ButtonFlex2(self):
		self._getter_access_tracker["ButtonFlex2"] = {}
		return self._ButtonFlex2
	@ButtonFlex2.setter
	def ButtonFlex2(self, new_state):
		self._setter_access_tracker["ButtonFlex2"] = {}
		self._ButtonFlex2 = ButtonFlex(new_state)

	@property
	def Anchor3(self):
		self._getter_access_tracker["Anchor3"] = {}
		return self._Anchor3
	@Anchor3.setter
	def Anchor3(self, new_state):
		self._setter_access_tracker["Anchor3"] = {}
		self._Anchor3 = Anchor(new_state)

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
	def Div4(self):
		self._getter_access_tracker["Div4"] = {}
		return self._Div4
	@Div4.setter
	def Div4(self, new_state):
		self._setter_access_tracker["Div4"] = {}
		self._Div4 = Div(new_state)

	@property
	def Flex10(self):
		self._getter_access_tracker["Flex10"] = {}
		return self._Flex10
	@Flex10.setter
	def Flex10(self, new_state):
		self._setter_access_tracker["Flex10"] = {}
		self._Flex10 = Flex(new_state)

	@property
	def ButtonFlex3(self):
		self._getter_access_tracker["ButtonFlex3"] = {}
		return self._ButtonFlex3
	@ButtonFlex3.setter
	def ButtonFlex3(self, new_state):
		self._setter_access_tracker["ButtonFlex3"] = {}
		self._ButtonFlex3 = ButtonFlex(new_state)

	@property
	def Anchor4(self):
		self._getter_access_tracker["Anchor4"] = {}
		return self._Anchor4
	@Anchor4.setter
	def Anchor4(self, new_state):
		self._setter_access_tracker["Anchor4"] = {}
		self._Anchor4 = Anchor(new_state)

	@property
	def Div5(self):
		self._getter_access_tracker["Div5"] = {}
		return self._Div5
	@Div5.setter
	def Div5(self, new_state):
		self._setter_access_tracker["Div5"] = {}
		self._Div5 = Div(new_state)

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
	def TextBox18(self):
		self._getter_access_tracker["TextBox18"] = {}
		return self._TextBox18
	@TextBox18.setter
	def TextBox18(self, new_state):
		self._setter_access_tracker["TextBox18"] = {}
		self._TextBox18 = TextBox(new_state)

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
	def Flex11(self):
		self._getter_access_tracker["Flex11"] = {}
		return self._Flex11
	@Flex11.setter
	def Flex11(self, new_state):
		self._setter_access_tracker["Flex11"] = {}
		self._Flex11 = Flex(new_state)

	@property
	def Flex12(self):
		self._getter_access_tracker["Flex12"] = {}
		return self._Flex12
	@Flex12.setter
	def Flex12(self, new_state):
		self._setter_access_tracker["Flex12"] = {}
		self._Flex12 = Flex(new_state)

	@property
	def FramerFlex5(self):
		self._getter_access_tracker["FramerFlex5"] = {}
		return self._FramerFlex5
	@FramerFlex5.setter
	def FramerFlex5(self, new_state):
		self._setter_access_tracker["FramerFlex5"] = {}
		self._FramerFlex5 = FramerFlex(new_state)

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
	def TextBox21(self):
		self._getter_access_tracker["TextBox21"] = {}
		return self._TextBox21
	@TextBox21.setter
	def TextBox21(self, new_state):
		self._setter_access_tracker["TextBox21"] = {}
		self._TextBox21 = TextBox(new_state)

	@property
	def FramerText1(self):
		self._getter_access_tracker["FramerText1"] = {}
		return self._FramerText1
	@FramerText1.setter
	def FramerText1(self, new_state):
		self._setter_access_tracker["FramerText1"] = {}
		self._FramerText1 = FramerText(new_state)

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
	def Anchor8(self):
		self._getter_access_tracker["Anchor8"] = {}
		return self._Anchor8
	@Anchor8.setter
	def Anchor8(self, new_state):
		self._setter_access_tracker["Anchor8"] = {}
		self._Anchor8 = Anchor(new_state)

	@property
	def FramerText4(self):
		self._getter_access_tracker["FramerText4"] = {}
		return self._FramerText4
	@FramerText4.setter
	def FramerText4(self, new_state):
		self._setter_access_tracker["FramerText4"] = {}
		self._FramerText4 = FramerText(new_state)

	@property
	def Anchor9(self):
		self._getter_access_tracker["Anchor9"] = {}
		return self._Anchor9
	@Anchor9.setter
	def Anchor9(self, new_state):
		self._setter_access_tracker["Anchor9"] = {}
		self._Anchor9 = Anchor(new_state)

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
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

	@property
	def Flex17(self):
		self._getter_access_tracker["Flex17"] = {}
		return self._Flex17
	@Flex17.setter
	def Flex17(self, new_state):
		self._setter_access_tracker["Flex17"] = {}
		self._Flex17 = Flex(new_state)

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
	def Flex18(self):
		self._getter_access_tracker["Flex18"] = {}
		return self._Flex18
	@Flex18.setter
	def Flex18(self, new_state):
		self._setter_access_tracker["Flex18"] = {}
		self._Flex18 = Flex(new_state)

	@property
	def TextBox24(self):
		self._getter_access_tracker["TextBox24"] = {}
		return self._TextBox24
	@TextBox24.setter
	def TextBox24(self, new_state):
		self._setter_access_tracker["TextBox24"] = {}
		self._TextBox24 = TextBox(new_state)

	@property
	def Div8(self):
		self._getter_access_tracker["Div8"] = {}
		return self._Div8
	@Div8.setter
	def Div8(self, new_state):
		self._setter_access_tracker["Div8"] = {}
		self._Div8 = Div(new_state)

	@property
	def Image3(self):
		self._getter_access_tracker["Image3"] = {}
		return self._Image3
	@Image3.setter
	def Image3(self, new_state):
		self._setter_access_tracker["Image3"] = {}
		self._Image3 = Image(new_state)

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
	def ScaleFlex2(self):
		self._getter_access_tracker["ScaleFlex2"] = {}
		return self._ScaleFlex2
	@ScaleFlex2.setter
	def ScaleFlex2(self, new_state):
		self._setter_access_tracker["ScaleFlex2"] = {}
		self._ScaleFlex2 = ScaleFlex(new_state)

	@property
	def article1(self):
		self._getter_access_tracker["article1"] = {}
		return self._article1
	@article1.setter
	def article1(self, new_state):
		self._setter_access_tracker["article1"] = {}
		self._article1 = Anchor(new_state)

	@property
	def FramerFlex6(self):
		self._getter_access_tracker["FramerFlex6"] = {}
		return self._FramerFlex6
	@FramerFlex6.setter
	def FramerFlex6(self, new_state):
		self._setter_access_tracker["FramerFlex6"] = {}
		self._FramerFlex6 = FramerFlex(new_state)

	@property
	def Image8(self):
		self._getter_access_tracker["Image8"] = {}
		return self._Image8
	@Image8.setter
	def Image8(self, new_state):
		self._setter_access_tracker["Image8"] = {}
		self._Image8 = Image(new_state)

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
	def Flex29(self):
		self._getter_access_tracker["Flex29"] = {}
		return self._Flex29
	@Flex29.setter
	def Flex29(self, new_state):
		self._setter_access_tracker["Flex29"] = {}
		self._Flex29 = Flex(new_state)

	@property
	def Image9(self):
		self._getter_access_tracker["Image9"] = {}
		return self._Image9
	@Image9.setter
	def Image9(self, new_state):
		self._setter_access_tracker["Image9"] = {}
		self._Image9 = Image(new_state)

	@property
	def Div11(self):
		self._getter_access_tracker["Div11"] = {}
		return self._Div11
	@Div11.setter
	def Div11(self, new_state):
		self._setter_access_tracker["Div11"] = {}
		self._Div11 = Div(new_state)

	@property
	def TextBox33(self):
		self._getter_access_tracker["TextBox33"] = {}
		return self._TextBox33
	@TextBox33.setter
	def TextBox33(self, new_state):
		self._setter_access_tracker["TextBox33"] = {}
		self._TextBox33 = TextBox(new_state)

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
	def ScaleFlex5(self):
		self._getter_access_tracker["ScaleFlex5"] = {}
		return self._ScaleFlex5
	@ScaleFlex5.setter
	def ScaleFlex5(self, new_state):
		self._setter_access_tracker["ScaleFlex5"] = {}
		self._ScaleFlex5 = ScaleFlex(new_state)

	@property
	def Anchor13(self):
		self._getter_access_tracker["Anchor13"] = {}
		return self._Anchor13
	@Anchor13.setter
	def Anchor13(self, new_state):
		self._setter_access_tracker["Anchor13"] = {}
		self._Anchor13 = Anchor(new_state)

	@property
	def FramerFlex9(self):
		self._getter_access_tracker["FramerFlex9"] = {}
		return self._FramerFlex9
	@FramerFlex9.setter
	def FramerFlex9(self, new_state):
		self._setter_access_tracker["FramerFlex9"] = {}
		self._FramerFlex9 = FramerFlex(new_state)

	@property
	def Image10(self):
		self._getter_access_tracker["Image10"] = {}
		return self._Image10
	@Image10.setter
	def Image10(self, new_state):
		self._setter_access_tracker["Image10"] = {}
		self._Image10 = Image(new_state)

	@property
	def TextBox34(self):
		self._getter_access_tracker["TextBox34"] = {}
		return self._TextBox34
	@TextBox34.setter
	def TextBox34(self, new_state):
		self._setter_access_tracker["TextBox34"] = {}
		self._TextBox34 = TextBox(new_state)

	@property
	def TextBox35(self):
		self._getter_access_tracker["TextBox35"] = {}
		return self._TextBox35
	@TextBox35.setter
	def TextBox35(self, new_state):
		self._setter_access_tracker["TextBox35"] = {}
		self._TextBox35 = TextBox(new_state)

	@property
	def Flex33(self):
		self._getter_access_tracker["Flex33"] = {}
		return self._Flex33
	@Flex33.setter
	def Flex33(self, new_state):
		self._setter_access_tracker["Flex33"] = {}
		self._Flex33 = Flex(new_state)

	@property
	def Image11(self):
		self._getter_access_tracker["Image11"] = {}
		return self._Image11
	@Image11.setter
	def Image11(self, new_state):
		self._setter_access_tracker["Image11"] = {}
		self._Image11 = Image(new_state)

	@property
	def Div12(self):
		self._getter_access_tracker["Div12"] = {}
		return self._Div12
	@Div12.setter
	def Div12(self, new_state):
		self._setter_access_tracker["Div12"] = {}
		self._Div12 = Div(new_state)

	@property
	def TextBox36(self):
		self._getter_access_tracker["TextBox36"] = {}
		return self._TextBox36
	@TextBox36.setter
	def TextBox36(self, new_state):
		self._setter_access_tracker["TextBox36"] = {}
		self._TextBox36 = TextBox(new_state)

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
	def Flex36(self):
		self._getter_access_tracker["Flex36"] = {}
		return self._Flex36
	@Flex36.setter
	def Flex36(self, new_state):
		self._setter_access_tracker["Flex36"] = {}
		self._Flex36 = Flex(new_state)

	@property
	def ScaleFlex6(self):
		self._getter_access_tracker["ScaleFlex6"] = {}
		return self._ScaleFlex6
	@ScaleFlex6.setter
	def ScaleFlex6(self, new_state):
		self._setter_access_tracker["ScaleFlex6"] = {}
		self._ScaleFlex6 = ScaleFlex(new_state)

	@property
	def Anchor14(self):
		self._getter_access_tracker["Anchor14"] = {}
		return self._Anchor14
	@Anchor14.setter
	def Anchor14(self, new_state):
		self._setter_access_tracker["Anchor14"] = {}
		self._Anchor14 = Anchor(new_state)

	@property
	def FramerFlex10(self):
		self._getter_access_tracker["FramerFlex10"] = {}
		return self._FramerFlex10
	@FramerFlex10.setter
	def FramerFlex10(self, new_state):
		self._setter_access_tracker["FramerFlex10"] = {}
		self._FramerFlex10 = FramerFlex(new_state)

	@property
	def Image12(self):
		self._getter_access_tracker["Image12"] = {}
		return self._Image12
	@Image12.setter
	def Image12(self, new_state):
		self._setter_access_tracker["Image12"] = {}
		self._Image12 = Image(new_state)

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
	def Flex37(self):
		self._getter_access_tracker["Flex37"] = {}
		return self._Flex37
	@Flex37.setter
	def Flex37(self, new_state):
		self._setter_access_tracker["Flex37"] = {}
		self._Flex37 = Flex(new_state)

	@property
	def Image13(self):
		self._getter_access_tracker["Image13"] = {}
		return self._Image13
	@Image13.setter
	def Image13(self, new_state):
		self._setter_access_tracker["Image13"] = {}
		self._Image13 = Image(new_state)

	@property
	def Div13(self):
		self._getter_access_tracker["Div13"] = {}
		return self._Div13
	@Div13.setter
	def Div13(self, new_state):
		self._setter_access_tracker["Div13"] = {}
		self._Div13 = Div(new_state)

	@property
	def TextBox39(self):
		self._getter_access_tracker["TextBox39"] = {}
		return self._TextBox39
	@TextBox39.setter
	def TextBox39(self, new_state):
		self._setter_access_tracker["TextBox39"] = {}
		self._TextBox39 = TextBox(new_state)

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
	def ScaleFlex7(self):
		self._getter_access_tracker["ScaleFlex7"] = {}
		return self._ScaleFlex7
	@ScaleFlex7.setter
	def ScaleFlex7(self, new_state):
		self._setter_access_tracker["ScaleFlex7"] = {}
		self._ScaleFlex7 = ScaleFlex(new_state)

	@property
	def Anchor15(self):
		self._getter_access_tracker["Anchor15"] = {}
		return self._Anchor15
	@Anchor15.setter
	def Anchor15(self, new_state):
		self._setter_access_tracker["Anchor15"] = {}
		self._Anchor15 = Anchor(new_state)

	@property
	def FramerFlex11(self):
		self._getter_access_tracker["FramerFlex11"] = {}
		return self._FramerFlex11
	@FramerFlex11.setter
	def FramerFlex11(self, new_state):
		self._setter_access_tracker["FramerFlex11"] = {}
		self._FramerFlex11 = FramerFlex(new_state)

	@property
	def Image14(self):
		self._getter_access_tracker["Image14"] = {}
		return self._Image14
	@Image14.setter
	def Image14(self, new_state):
		self._setter_access_tracker["Image14"] = {}
		self._Image14 = Image(new_state)

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
	def Flex41(self):
		self._getter_access_tracker["Flex41"] = {}
		return self._Flex41
	@Flex41.setter
	def Flex41(self, new_state):
		self._setter_access_tracker["Flex41"] = {}
		self._Flex41 = Flex(new_state)

	@property
	def Image15(self):
		self._getter_access_tracker["Image15"] = {}
		return self._Image15
	@Image15.setter
	def Image15(self, new_state):
		self._setter_access_tracker["Image15"] = {}
		self._Image15 = Image(new_state)

	@property
	def Div14(self):
		self._getter_access_tracker["Div14"] = {}
		return self._Div14
	@Div14.setter
	def Div14(self, new_state):
		self._setter_access_tracker["Div14"] = {}
		self._Div14 = Div(new_state)

	@property
	def TextBox42(self):
		self._getter_access_tracker["TextBox42"] = {}
		return self._TextBox42
	@TextBox42.setter
	def TextBox42(self, new_state):
		self._setter_access_tracker["TextBox42"] = {}
		self._TextBox42 = TextBox(new_state)

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
	def Flex44(self):
		self._getter_access_tracker["Flex44"] = {}
		return self._Flex44
	@Flex44.setter
	def Flex44(self, new_state):
		self._setter_access_tracker["Flex44"] = {}
		self._Flex44 = Flex(new_state)

	@property
	def ScaleFlex8(self):
		self._getter_access_tracker["ScaleFlex8"] = {}
		return self._ScaleFlex8
	@ScaleFlex8.setter
	def ScaleFlex8(self, new_state):
		self._setter_access_tracker["ScaleFlex8"] = {}
		self._ScaleFlex8 = ScaleFlex(new_state)

	@property
	def Anchor16(self):
		self._getter_access_tracker["Anchor16"] = {}
		return self._Anchor16
	@Anchor16.setter
	def Anchor16(self, new_state):
		self._setter_access_tracker["Anchor16"] = {}
		self._Anchor16 = Anchor(new_state)

	@property
	def FramerFlex12(self):
		self._getter_access_tracker["FramerFlex12"] = {}
		return self._FramerFlex12
	@FramerFlex12.setter
	def FramerFlex12(self, new_state):
		self._setter_access_tracker["FramerFlex12"] = {}
		self._FramerFlex12 = FramerFlex(new_state)

	@property
	def Image16(self):
		self._getter_access_tracker["Image16"] = {}
		return self._Image16
	@Image16.setter
	def Image16(self, new_state):
		self._setter_access_tracker["Image16"] = {}
		self._Image16 = Image(new_state)

	@property
	def TextBox43(self):
		self._getter_access_tracker["TextBox43"] = {}
		return self._TextBox43
	@TextBox43.setter
	def TextBox43(self, new_state):
		self._setter_access_tracker["TextBox43"] = {}
		self._TextBox43 = TextBox(new_state)

	@property
	def TextBox44(self):
		self._getter_access_tracker["TextBox44"] = {}
		return self._TextBox44
	@TextBox44.setter
	def TextBox44(self, new_state):
		self._setter_access_tracker["TextBox44"] = {}
		self._TextBox44 = TextBox(new_state)

	@property
	def Flex45(self):
		self._getter_access_tracker["Flex45"] = {}
		return self._Flex45
	@Flex45.setter
	def Flex45(self, new_state):
		self._setter_access_tracker["Flex45"] = {}
		self._Flex45 = Flex(new_state)

	@property
	def Image17(self):
		self._getter_access_tracker["Image17"] = {}
		return self._Image17
	@Image17.setter
	def Image17(self, new_state):
		self._setter_access_tracker["Image17"] = {}
		self._Image17 = Image(new_state)

	@property
	def Div15(self):
		self._getter_access_tracker["Div15"] = {}
		return self._Div15
	@Div15.setter
	def Div15(self, new_state):
		self._setter_access_tracker["Div15"] = {}
		self._Div15 = Div(new_state)

	@property
	def TextBox45(self):
		self._getter_access_tracker["TextBox45"] = {}
		return self._TextBox45
	@TextBox45.setter
	def TextBox45(self, new_state):
		self._setter_access_tracker["TextBox45"] = {}
		self._TextBox45 = TextBox(new_state)

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
	def ScaleFlex9(self):
		self._getter_access_tracker["ScaleFlex9"] = {}
		return self._ScaleFlex9
	@ScaleFlex9.setter
	def ScaleFlex9(self, new_state):
		self._setter_access_tracker["ScaleFlex9"] = {}
		self._ScaleFlex9 = ScaleFlex(new_state)

	@property
	def Anchor17(self):
		self._getter_access_tracker["Anchor17"] = {}
		return self._Anchor17
	@Anchor17.setter
	def Anchor17(self, new_state):
		self._setter_access_tracker["Anchor17"] = {}
		self._Anchor17 = Anchor(new_state)

	@property
	def FramerFlex13(self):
		self._getter_access_tracker["FramerFlex13"] = {}
		return self._FramerFlex13
	@FramerFlex13.setter
	def FramerFlex13(self, new_state):
		self._setter_access_tracker["FramerFlex13"] = {}
		self._FramerFlex13 = FramerFlex(new_state)

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
	def FramerFlex14(self):
		self._getter_access_tracker["FramerFlex14"] = {}
		return self._FramerFlex14
	@FramerFlex14.setter
	def FramerFlex14(self, new_state):
		self._setter_access_tracker["FramerFlex14"] = {}
		self._FramerFlex14 = FramerFlex(new_state)

	@property
	def TextBox46(self):
		self._getter_access_tracker["TextBox46"] = {}
		return self._TextBox46
	@TextBox46.setter
	def TextBox46(self, new_state):
		self._setter_access_tracker["TextBox46"] = {}
		self._TextBox46 = TextBox(new_state)

	@property
	def Input1(self):
		self._getter_access_tracker["Input1"] = {}
		return self._Input1
	@Input1.setter
	def Input1(self, new_state):
		self._setter_access_tracker["Input1"] = {}
		self._Input1 = Input(new_state)

	@property
	def ButtonFlex4(self):
		self._getter_access_tracker["ButtonFlex4"] = {}
		return self._ButtonFlex4
	@ButtonFlex4.setter
	def ButtonFlex4(self, new_state):
		self._setter_access_tracker["ButtonFlex4"] = {}
		self._ButtonFlex4 = ButtonFlex(new_state)

	@property
	def FramerText5(self):
		self._getter_access_tracker["FramerText5"] = {}
		return self._FramerText5
	@FramerText5.setter
	def FramerText5(self, new_state):
		self._setter_access_tracker["FramerText5"] = {}
		self._FramerText5 = FramerText(new_state)

	@property
	def Flex52(self):
		self._getter_access_tracker["Flex52"] = {}
		return self._Flex52
	@Flex52.setter
	def Flex52(self, new_state):
		self._setter_access_tracker["Flex52"] = {}
		self._Flex52 = Flex(new_state)
  
	def _to_json_fields(self):
		return {
			"Flex1": self._Flex1,
			"Flex2": self._Flex2,
			"FramerFlex1": self._FramerFlex1,
			"Flex3": self._Flex3,
			"TextBox1": self._TextBox1,
			"FramerFlex3": self._FramerFlex3,
			"Anchor1": self._Anchor1,
			"ScaleFlex1": self._ScaleFlex1,
			"FramerFlex4": self._FramerFlex4,
			"Flex4": self._Flex4,
			"Flex5": self._Flex5,
			"Image1": self._Image1,
			"Flex6": self._Flex6,
			"TextBox4": self._TextBox4,
			"TextBox5": self._TextBox5,
			"Div1": self._Div1,
			"TextBox6": self._TextBox6,
			"ButtonFlex1": self._ButtonFlex1,
			"Div2": self._Div2,
			"Flex8": self._Flex8,
			"TextBox9": self._TextBox9,
			"TextBox10": self._TextBox10,
			"Anchor2": self._Anchor2,
			"TextBox12": self._TextBox12,
			"TextBox13": self._TextBox13,
			"Div3": self._Div3,
			"Flex9": self._Flex9,
			"ButtonFlex2": self._ButtonFlex2,
			"Anchor3": self._Anchor3,
			"TextBox15": self._TextBox15,
			"TextBox16": self._TextBox16,
			"Div4": self._Div4,
			"Flex10": self._Flex10,
			"ButtonFlex3": self._ButtonFlex3,
			"Anchor4": self._Anchor4,
			"Div5": self._Div5,
			"Div6": self._Div6,
			"Div7": self._Div7,
			"TextBox18": self._TextBox18,
			"TextBox19": self._TextBox19,
			"TextBox20": self._TextBox20,
			"Flex11": self._Flex11,
			"Flex12": self._Flex12,
			"FramerFlex5": self._FramerFlex5,
			"Flex13": self._Flex13,
			"Flex14": self._Flex14,
			"TextBox21": self._TextBox21,
			"FramerText1": self._FramerText1,
			"Anchor6": self._Anchor6,
			"Anchor7": self._Anchor7,
			"FramerText2": self._FramerText2,
			"FramerText3": self._FramerText3,
			"Anchor8": self._Anchor8,
			"FramerText4": self._FramerText4,
			"Anchor9": self._Anchor9,
			"Flex15": self._Flex15,
			"Flex16": self._Flex16,
			"Image2": self._Image2,
			"Flex17": self._Flex17,
			"TextBox22": self._TextBox22,
			"TextBox23": self._TextBox23,
			"Flex18": self._Flex18,
			"TextBox24": self._TextBox24,
			"Div8": self._Div8,
			"Image3": self._Image3,
			"Flex19": self._Flex19,
			"Flex20": self._Flex20,
			"ScaleFlex2": self._ScaleFlex2,
			"article1": self._article1,
			"FramerFlex6": self._FramerFlex6,
			"Image8": self._Image8,
			"TextBox31": self._TextBox31,
			"TextBox32": self._TextBox32,
			"Flex29": self._Flex29,
			"Image9": self._Image9,
			"Div11": self._Div11,
			"TextBox33": self._TextBox33,
			"Flex30": self._Flex30,
			"Flex31": self._Flex31,
			"Flex32": self._Flex32,
			"ScaleFlex5": self._ScaleFlex5,
			"Anchor13": self._Anchor13,
			"FramerFlex9": self._FramerFlex9,
			"Image10": self._Image10,
			"TextBox34": self._TextBox34,
			"TextBox35": self._TextBox35,
			"Flex33": self._Flex33,
			"Image11": self._Image11,
			"Div12": self._Div12,
			"TextBox36": self._TextBox36,
			"Flex34": self._Flex34,
			"Flex35": self._Flex35,
			"Flex36": self._Flex36,
			"ScaleFlex6": self._ScaleFlex6,
			"Anchor14": self._Anchor14,
			"FramerFlex10": self._FramerFlex10,
			"Image12": self._Image12,
			"TextBox37": self._TextBox37,
			"TextBox38": self._TextBox38,
			"Flex37": self._Flex37,
			"Image13": self._Image13,
			"Div13": self._Div13,
			"TextBox39": self._TextBox39,
			"Flex38": self._Flex38,
			"Flex39": self._Flex39,
			"Flex40": self._Flex40,
			"ScaleFlex7": self._ScaleFlex7,
			"Anchor15": self._Anchor15,
			"FramerFlex11": self._FramerFlex11,
			"Image14": self._Image14,
			"TextBox40": self._TextBox40,
			"TextBox41": self._TextBox41,
			"Flex41": self._Flex41,
			"Image15": self._Image15,
			"Div14": self._Div14,
			"TextBox42": self._TextBox42,
			"Flex42": self._Flex42,
			"Flex43": self._Flex43,
			"Flex44": self._Flex44,
			"ScaleFlex8": self._ScaleFlex8,
			"Anchor16": self._Anchor16,
			"FramerFlex12": self._FramerFlex12,
			"Image16": self._Image16,
			"TextBox43": self._TextBox43,
			"TextBox44": self._TextBox44,
			"Flex45": self._Flex45,
			"Image17": self._Image17,
			"Div15": self._Div15,
			"TextBox45": self._TextBox45,
			"Flex46": self._Flex46,
			"Flex47": self._Flex47,
			"Flex48": self._Flex48,
			"ScaleFlex9": self._ScaleFlex9,
			"Anchor17": self._Anchor17,
			"FramerFlex13": self._FramerFlex13,
			"Flex49": self._Flex49,
			"Flex50": self._Flex50,
			"FramerFlex14": self._FramerFlex14,
			"TextBox46": self._TextBox46,
			"Input1": self._Input1,
			"ButtonFlex4": self._ButtonFlex4,
			"FramerText5": self._FramerText5,
			"Flex52": self._Flex52
			}
  