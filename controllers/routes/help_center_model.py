from typing import Union, Any
from atri_react.Flex import Flex
from manifests.FramerFlex import FramerFlex
from atri_react.TextBox import TextBox
from atri_react.Anchor import Anchor
from manifests.ScaleFlex import ScaleFlex
from manifests.ButtonFlex import ButtonFlex
from atri_react.Image import Image
from atri_react.Div import Div
from manifests.FramerText import FramerText


  
class Page:
	def __init__(self, state: Union[Any, None]):
		self.event_data = None
		self.event_alias = None
		self._setter_access_tracker = {}
		self.Flex1 = state["Flex1"] if "Flex1" in state else None
		self.Flex2 = state["Flex2"] if "Flex2" in state else None
		self.FramerFlex1 = state["FramerFlex1"] if "FramerFlex1" in state else None
		self.TextBox1 = state["TextBox1"] if "TextBox1" in state else None
		self.TextBox2 = state["TextBox2"] if "TextBox2" in state else None
		self.Flex3 = state["Flex3"] if "Flex3" in state else None
		self.Flex4 = state["Flex4"] if "Flex4" in state else None
		self.Flex5 = state["Flex5"] if "Flex5" in state else None
		self.Flex6 = state["Flex6"] if "Flex6" in state else None
		self.FramerFlex2 = state["FramerFlex2"] if "FramerFlex2" in state else None
		self.Anchor1 = state["Anchor1"] if "Anchor1" in state else None
		self.ScaleFlex1 = state["ScaleFlex1"] if "ScaleFlex1" in state else None
		self.Flex7 = state["Flex7"] if "Flex7" in state else None
		self.ButtonFlex1 = state["ButtonFlex1"] if "ButtonFlex1" in state else None
		self.Flex8 = state["Flex8"] if "Flex8" in state else None
		self.Image1 = state["Image1"] if "Image1" in state else None
		self.TextBox3 = state["TextBox3"] if "TextBox3" in state else None
		self.TextBox4 = state["TextBox4"] if "TextBox4" in state else None
		self.TextBox5 = state["TextBox5"] if "TextBox5" in state else None
		self.TextBox6 = state["TextBox6"] if "TextBox6" in state else None
		self.TextBox7 = state["TextBox7"] if "TextBox7" in state else None
		self.TextBox8 = state["TextBox8"] if "TextBox8" in state else None
		self.TextBox9 = state["TextBox9"] if "TextBox9" in state else None
		self.TextBox10 = state["TextBox10"] if "TextBox10" in state else None
		self.Image2 = state["Image2"] if "Image2" in state else None
		self.Flex9 = state["Flex9"] if "Flex9" in state else None
		self.ButtonFlex2 = state["ButtonFlex2"] if "ButtonFlex2" in state else None
		self.Flex10 = state["Flex10"] if "Flex10" in state else None
		self.ScaleFlex2 = state["ScaleFlex2"] if "ScaleFlex2" in state else None
		self.Anchor2 = state["Anchor2"] if "Anchor2" in state else None
		self.FramerFlex3 = state["FramerFlex3"] if "FramerFlex3" in state else None
		self.TextBox11 = state["TextBox11"] if "TextBox11" in state else None
		self.TextBox12 = state["TextBox12"] if "TextBox12" in state else None
		self.TextBox13 = state["TextBox13"] if "TextBox13" in state else None
		self.TextBox14 = state["TextBox14"] if "TextBox14" in state else None
		self.Image3 = state["Image3"] if "Image3" in state else None
		self.Flex11 = state["Flex11"] if "Flex11" in state else None
		self.ButtonFlex3 = state["ButtonFlex3"] if "ButtonFlex3" in state else None
		self.Flex12 = state["Flex12"] if "Flex12" in state else None
		self.ScaleFlex3 = state["ScaleFlex3"] if "ScaleFlex3" in state else None
		self.Anchor3 = state["Anchor3"] if "Anchor3" in state else None
		self.FramerFlex4 = state["FramerFlex4"] if "FramerFlex4" in state else None
		self.TextBox15 = state["TextBox15"] if "TextBox15" in state else None
		self.TextBox16 = state["TextBox16"] if "TextBox16" in state else None
		self.TextBox17 = state["TextBox17"] if "TextBox17" in state else None
		self.TextBox18 = state["TextBox18"] if "TextBox18" in state else None
		self.Image4 = state["Image4"] if "Image4" in state else None
		self.Flex13 = state["Flex13"] if "Flex13" in state else None
		self.ButtonFlex4 = state["ButtonFlex4"] if "ButtonFlex4" in state else None
		self.Flex14 = state["Flex14"] if "Flex14" in state else None
		self.ScaleFlex4 = state["ScaleFlex4"] if "ScaleFlex4" in state else None
		self.Anchor4 = state["Anchor4"] if "Anchor4" in state else None
		self.FramerFlex5 = state["FramerFlex5"] if "FramerFlex5" in state else None
		self.TextBox19 = state["TextBox19"] if "TextBox19" in state else None
		self.TextBox20 = state["TextBox20"] if "TextBox20" in state else None
		self.TextBox21 = state["TextBox21"] if "TextBox21" in state else None
		self.TextBox22 = state["TextBox22"] if "TextBox22" in state else None
		self.Image5 = state["Image5"] if "Image5" in state else None
		self.Flex15 = state["Flex15"] if "Flex15" in state else None
		self.ButtonFlex5 = state["ButtonFlex5"] if "ButtonFlex5" in state else None
		self.Flex16 = state["Flex16"] if "Flex16" in state else None
		self.ScaleFlex5 = state["ScaleFlex5"] if "ScaleFlex5" in state else None
		self.Anchor5 = state["Anchor5"] if "Anchor5" in state else None
		self.FramerFlex6 = state["FramerFlex6"] if "FramerFlex6" in state else None
		self.TextBox23 = state["TextBox23"] if "TextBox23" in state else None
		self.TextBox24 = state["TextBox24"] if "TextBox24" in state else None
		self.TextBox25 = state["TextBox25"] if "TextBox25" in state else None
		self.TextBox26 = state["TextBox26"] if "TextBox26" in state else None
		self.Image6 = state["Image6"] if "Image6" in state else None
		self.Flex17 = state["Flex17"] if "Flex17" in state else None
		self.ButtonFlex6 = state["ButtonFlex6"] if "ButtonFlex6" in state else None
		self.Flex18 = state["Flex18"] if "Flex18" in state else None
		self.ScaleFlex6 = state["ScaleFlex6"] if "ScaleFlex6" in state else None
		self.Anchor6 = state["Anchor6"] if "Anchor6" in state else None
		self.FramerFlex7 = state["FramerFlex7"] if "FramerFlex7" in state else None
		self.Flex19 = state["Flex19"] if "Flex19" in state else None
		self.Flex20 = state["Flex20"] if "Flex20" in state else None
		self.FramerFlex8 = state["FramerFlex8"] if "FramerFlex8" in state else None
		self.Flex21 = state["Flex21"] if "Flex21" in state else None
		self.Flex22 = state["Flex22"] if "Flex22" in state else None
		self.Div1 = state["Div1"] if "Div1" in state else None
		self.TextBox27 = state["TextBox27"] if "TextBox27" in state else None
		self.Anchor7 = state["Anchor7"] if "Anchor7" in state else None
		self.Flex23 = state["Flex23"] if "Flex23" in state else None
		self.TextBox28 = state["TextBox28"] if "TextBox28" in state else None
		self.FramerText1 = state["FramerText1"] if "FramerText1" in state else None
		self.FramerText2 = state["FramerText2"] if "FramerText2" in state else None
		self.TextBox30 = state["TextBox30"] if "TextBox30" in state else None
		self.Anchor8 = state["Anchor8"] if "Anchor8" in state else None
		self.Flex24 = state["Flex24"] if "Flex24" in state else None
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
	def Flex3(self):
		self._getter_access_tracker["Flex3"] = {}
		return self._Flex3
	@Flex3.setter
	def Flex3(self, new_state):
		self._setter_access_tracker["Flex3"] = {}
		self._Flex3 = Flex(new_state)

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
	def Flex6(self):
		self._getter_access_tracker["Flex6"] = {}
		return self._Flex6
	@Flex6.setter
	def Flex6(self, new_state):
		self._setter_access_tracker["Flex6"] = {}
		self._Flex6 = Flex(new_state)

	@property
	def FramerFlex2(self):
		self._getter_access_tracker["FramerFlex2"] = {}
		return self._FramerFlex2
	@FramerFlex2.setter
	def FramerFlex2(self, new_state):
		self._setter_access_tracker["FramerFlex2"] = {}
		self._FramerFlex2 = FramerFlex(new_state)

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
	def Flex7(self):
		self._getter_access_tracker["Flex7"] = {}
		return self._Flex7
	@Flex7.setter
	def Flex7(self, new_state):
		self._setter_access_tracker["Flex7"] = {}
		self._Flex7 = Flex(new_state)

	@property
	def ButtonFlex1(self):
		self._getter_access_tracker["ButtonFlex1"] = {}
		return self._ButtonFlex1
	@ButtonFlex1.setter
	def ButtonFlex1(self, new_state):
		self._setter_access_tracker["ButtonFlex1"] = {}
		self._ButtonFlex1 = ButtonFlex(new_state)

	@property
	def Flex8(self):
		self._getter_access_tracker["Flex8"] = {}
		return self._Flex8
	@Flex8.setter
	def Flex8(self, new_state):
		self._setter_access_tracker["Flex8"] = {}
		self._Flex8 = Flex(new_state)

	@property
	def Image1(self):
		self._getter_access_tracker["Image1"] = {}
		return self._Image1
	@Image1.setter
	def Image1(self, new_state):
		self._setter_access_tracker["Image1"] = {}
		self._Image1 = Image(new_state)

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
	def Image2(self):
		self._getter_access_tracker["Image2"] = {}
		return self._Image2
	@Image2.setter
	def Image2(self, new_state):
		self._setter_access_tracker["Image2"] = {}
		self._Image2 = Image(new_state)

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
	def Flex10(self):
		self._getter_access_tracker["Flex10"] = {}
		return self._Flex10
	@Flex10.setter
	def Flex10(self, new_state):
		self._setter_access_tracker["Flex10"] = {}
		self._Flex10 = Flex(new_state)

	@property
	def ScaleFlex2(self):
		self._getter_access_tracker["ScaleFlex2"] = {}
		return self._ScaleFlex2
	@ScaleFlex2.setter
	def ScaleFlex2(self, new_state):
		self._setter_access_tracker["ScaleFlex2"] = {}
		self._ScaleFlex2 = ScaleFlex(new_state)

	@property
	def Anchor2(self):
		self._getter_access_tracker["Anchor2"] = {}
		return self._Anchor2
	@Anchor2.setter
	def Anchor2(self, new_state):
		self._setter_access_tracker["Anchor2"] = {}
		self._Anchor2 = Anchor(new_state)

	@property
	def FramerFlex3(self):
		self._getter_access_tracker["FramerFlex3"] = {}
		return self._FramerFlex3
	@FramerFlex3.setter
	def FramerFlex3(self, new_state):
		self._setter_access_tracker["FramerFlex3"] = {}
		self._FramerFlex3 = FramerFlex(new_state)

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
	def TextBox13(self):
		self._getter_access_tracker["TextBox13"] = {}
		return self._TextBox13
	@TextBox13.setter
	def TextBox13(self, new_state):
		self._setter_access_tracker["TextBox13"] = {}
		self._TextBox13 = TextBox(new_state)

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
	def Flex11(self):
		self._getter_access_tracker["Flex11"] = {}
		return self._Flex11
	@Flex11.setter
	def Flex11(self, new_state):
		self._setter_access_tracker["Flex11"] = {}
		self._Flex11 = Flex(new_state)

	@property
	def ButtonFlex3(self):
		self._getter_access_tracker["ButtonFlex3"] = {}
		return self._ButtonFlex3
	@ButtonFlex3.setter
	def ButtonFlex3(self, new_state):
		self._setter_access_tracker["ButtonFlex3"] = {}
		self._ButtonFlex3 = ButtonFlex(new_state)

	@property
	def Flex12(self):
		self._getter_access_tracker["Flex12"] = {}
		return self._Flex12
	@Flex12.setter
	def Flex12(self, new_state):
		self._setter_access_tracker["Flex12"] = {}
		self._Flex12 = Flex(new_state)

	@property
	def ScaleFlex3(self):
		self._getter_access_tracker["ScaleFlex3"] = {}
		return self._ScaleFlex3
	@ScaleFlex3.setter
	def ScaleFlex3(self, new_state):
		self._setter_access_tracker["ScaleFlex3"] = {}
		self._ScaleFlex3 = ScaleFlex(new_state)

	@property
	def Anchor3(self):
		self._getter_access_tracker["Anchor3"] = {}
		return self._Anchor3
	@Anchor3.setter
	def Anchor3(self, new_state):
		self._setter_access_tracker["Anchor3"] = {}
		self._Anchor3 = Anchor(new_state)

	@property
	def FramerFlex4(self):
		self._getter_access_tracker["FramerFlex4"] = {}
		return self._FramerFlex4
	@FramerFlex4.setter
	def FramerFlex4(self, new_state):
		self._setter_access_tracker["FramerFlex4"] = {}
		self._FramerFlex4 = FramerFlex(new_state)

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
	def Image4(self):
		self._getter_access_tracker["Image4"] = {}
		return self._Image4
	@Image4.setter
	def Image4(self, new_state):
		self._setter_access_tracker["Image4"] = {}
		self._Image4 = Image(new_state)

	@property
	def Flex13(self):
		self._getter_access_tracker["Flex13"] = {}
		return self._Flex13
	@Flex13.setter
	def Flex13(self, new_state):
		self._setter_access_tracker["Flex13"] = {}
		self._Flex13 = Flex(new_state)

	@property
	def ButtonFlex4(self):
		self._getter_access_tracker["ButtonFlex4"] = {}
		return self._ButtonFlex4
	@ButtonFlex4.setter
	def ButtonFlex4(self, new_state):
		self._setter_access_tracker["ButtonFlex4"] = {}
		self._ButtonFlex4 = ButtonFlex(new_state)

	@property
	def Flex14(self):
		self._getter_access_tracker["Flex14"] = {}
		return self._Flex14
	@Flex14.setter
	def Flex14(self, new_state):
		self._setter_access_tracker["Flex14"] = {}
		self._Flex14 = Flex(new_state)

	@property
	def ScaleFlex4(self):
		self._getter_access_tracker["ScaleFlex4"] = {}
		return self._ScaleFlex4
	@ScaleFlex4.setter
	def ScaleFlex4(self, new_state):
		self._setter_access_tracker["ScaleFlex4"] = {}
		self._ScaleFlex4 = ScaleFlex(new_state)

	@property
	def Anchor4(self):
		self._getter_access_tracker["Anchor4"] = {}
		return self._Anchor4
	@Anchor4.setter
	def Anchor4(self, new_state):
		self._setter_access_tracker["Anchor4"] = {}
		self._Anchor4 = Anchor(new_state)

	@property
	def FramerFlex5(self):
		self._getter_access_tracker["FramerFlex5"] = {}
		return self._FramerFlex5
	@FramerFlex5.setter
	def FramerFlex5(self, new_state):
		self._setter_access_tracker["FramerFlex5"] = {}
		self._FramerFlex5 = FramerFlex(new_state)

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
	def Image5(self):
		self._getter_access_tracker["Image5"] = {}
		return self._Image5
	@Image5.setter
	def Image5(self, new_state):
		self._setter_access_tracker["Image5"] = {}
		self._Image5 = Image(new_state)

	@property
	def Flex15(self):
		self._getter_access_tracker["Flex15"] = {}
		return self._Flex15
	@Flex15.setter
	def Flex15(self, new_state):
		self._setter_access_tracker["Flex15"] = {}
		self._Flex15 = Flex(new_state)

	@property
	def ButtonFlex5(self):
		self._getter_access_tracker["ButtonFlex5"] = {}
		return self._ButtonFlex5
	@ButtonFlex5.setter
	def ButtonFlex5(self, new_state):
		self._setter_access_tracker["ButtonFlex5"] = {}
		self._ButtonFlex5 = ButtonFlex(new_state)

	@property
	def Flex16(self):
		self._getter_access_tracker["Flex16"] = {}
		return self._Flex16
	@Flex16.setter
	def Flex16(self, new_state):
		self._setter_access_tracker["Flex16"] = {}
		self._Flex16 = Flex(new_state)

	@property
	def ScaleFlex5(self):
		self._getter_access_tracker["ScaleFlex5"] = {}
		return self._ScaleFlex5
	@ScaleFlex5.setter
	def ScaleFlex5(self, new_state):
		self._setter_access_tracker["ScaleFlex5"] = {}
		self._ScaleFlex5 = ScaleFlex(new_state)

	@property
	def Anchor5(self):
		self._getter_access_tracker["Anchor5"] = {}
		return self._Anchor5
	@Anchor5.setter
	def Anchor5(self, new_state):
		self._setter_access_tracker["Anchor5"] = {}
		self._Anchor5 = Anchor(new_state)

	@property
	def FramerFlex6(self):
		self._getter_access_tracker["FramerFlex6"] = {}
		return self._FramerFlex6
	@FramerFlex6.setter
	def FramerFlex6(self, new_state):
		self._setter_access_tracker["FramerFlex6"] = {}
		self._FramerFlex6 = FramerFlex(new_state)

	@property
	def TextBox23(self):
		self._getter_access_tracker["TextBox23"] = {}
		return self._TextBox23
	@TextBox23.setter
	def TextBox23(self, new_state):
		self._setter_access_tracker["TextBox23"] = {}
		self._TextBox23 = TextBox(new_state)

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
	def TextBox26(self):
		self._getter_access_tracker["TextBox26"] = {}
		return self._TextBox26
	@TextBox26.setter
	def TextBox26(self, new_state):
		self._setter_access_tracker["TextBox26"] = {}
		self._TextBox26 = TextBox(new_state)

	@property
	def Image6(self):
		self._getter_access_tracker["Image6"] = {}
		return self._Image6
	@Image6.setter
	def Image6(self, new_state):
		self._setter_access_tracker["Image6"] = {}
		self._Image6 = Image(new_state)

	@property
	def Flex17(self):
		self._getter_access_tracker["Flex17"] = {}
		return self._Flex17
	@Flex17.setter
	def Flex17(self, new_state):
		self._setter_access_tracker["Flex17"] = {}
		self._Flex17 = Flex(new_state)

	@property
	def ButtonFlex6(self):
		self._getter_access_tracker["ButtonFlex6"] = {}
		return self._ButtonFlex6
	@ButtonFlex6.setter
	def ButtonFlex6(self, new_state):
		self._setter_access_tracker["ButtonFlex6"] = {}
		self._ButtonFlex6 = ButtonFlex(new_state)

	@property
	def Flex18(self):
		self._getter_access_tracker["Flex18"] = {}
		return self._Flex18
	@Flex18.setter
	def Flex18(self, new_state):
		self._setter_access_tracker["Flex18"] = {}
		self._Flex18 = Flex(new_state)

	@property
	def ScaleFlex6(self):
		self._getter_access_tracker["ScaleFlex6"] = {}
		return self._ScaleFlex6
	@ScaleFlex6.setter
	def ScaleFlex6(self, new_state):
		self._setter_access_tracker["ScaleFlex6"] = {}
		self._ScaleFlex6 = ScaleFlex(new_state)

	@property
	def Anchor6(self):
		self._getter_access_tracker["Anchor6"] = {}
		return self._Anchor6
	@Anchor6.setter
	def Anchor6(self, new_state):
		self._setter_access_tracker["Anchor6"] = {}
		self._Anchor6 = Anchor(new_state)

	@property
	def FramerFlex7(self):
		self._getter_access_tracker["FramerFlex7"] = {}
		return self._FramerFlex7
	@FramerFlex7.setter
	def FramerFlex7(self, new_state):
		self._setter_access_tracker["FramerFlex7"] = {}
		self._FramerFlex7 = FramerFlex(new_state)

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
	def FramerFlex8(self):
		self._getter_access_tracker["FramerFlex8"] = {}
		return self._FramerFlex8
	@FramerFlex8.setter
	def FramerFlex8(self, new_state):
		self._setter_access_tracker["FramerFlex8"] = {}
		self._FramerFlex8 = FramerFlex(new_state)

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
	def Div1(self):
		self._getter_access_tracker["Div1"] = {}
		return self._Div1
	@Div1.setter
	def Div1(self, new_state):
		self._setter_access_tracker["Div1"] = {}
		self._Div1 = Div(new_state)

	@property
	def TextBox27(self):
		self._getter_access_tracker["TextBox27"] = {}
		return self._TextBox27
	@TextBox27.setter
	def TextBox27(self, new_state):
		self._setter_access_tracker["TextBox27"] = {}
		self._TextBox27 = TextBox(new_state)

	@property
	def Anchor7(self):
		self._getter_access_tracker["Anchor7"] = {}
		return self._Anchor7
	@Anchor7.setter
	def Anchor7(self, new_state):
		self._setter_access_tracker["Anchor7"] = {}
		self._Anchor7 = Anchor(new_state)

	@property
	def Flex23(self):
		self._getter_access_tracker["Flex23"] = {}
		return self._Flex23
	@Flex23.setter
	def Flex23(self, new_state):
		self._setter_access_tracker["Flex23"] = {}
		self._Flex23 = Flex(new_state)

	@property
	def TextBox28(self):
		self._getter_access_tracker["TextBox28"] = {}
		return self._TextBox28
	@TextBox28.setter
	def TextBox28(self, new_state):
		self._setter_access_tracker["TextBox28"] = {}
		self._TextBox28 = TextBox(new_state)

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
	def TextBox30(self):
		self._getter_access_tracker["TextBox30"] = {}
		return self._TextBox30
	@TextBox30.setter
	def TextBox30(self, new_state):
		self._setter_access_tracker["TextBox30"] = {}
		self._TextBox30 = TextBox(new_state)

	@property
	def Anchor8(self):
		self._getter_access_tracker["Anchor8"] = {}
		return self._Anchor8
	@Anchor8.setter
	def Anchor8(self, new_state):
		self._setter_access_tracker["Anchor8"] = {}
		self._Anchor8 = Anchor(new_state)

	@property
	def Flex24(self):
		self._getter_access_tracker["Flex24"] = {}
		return self._Flex24
	@Flex24.setter
	def Flex24(self, new_state):
		self._setter_access_tracker["Flex24"] = {}
		self._Flex24 = Flex(new_state)
  
	def _to_json_fields(self):
		return {
			"Flex1": self._Flex1,
			"Flex2": self._Flex2,
			"FramerFlex1": self._FramerFlex1,
			"TextBox1": self._TextBox1,
			"TextBox2": self._TextBox2,
			"Flex3": self._Flex3,
			"Flex4": self._Flex4,
			"Flex5": self._Flex5,
			"Flex6": self._Flex6,
			"FramerFlex2": self._FramerFlex2,
			"Anchor1": self._Anchor1,
			"ScaleFlex1": self._ScaleFlex1,
			"Flex7": self._Flex7,
			"ButtonFlex1": self._ButtonFlex1,
			"Flex8": self._Flex8,
			"Image1": self._Image1,
			"TextBox3": self._TextBox3,
			"TextBox4": self._TextBox4,
			"TextBox5": self._TextBox5,
			"TextBox6": self._TextBox6,
			"TextBox7": self._TextBox7,
			"TextBox8": self._TextBox8,
			"TextBox9": self._TextBox9,
			"TextBox10": self._TextBox10,
			"Image2": self._Image2,
			"Flex9": self._Flex9,
			"ButtonFlex2": self._ButtonFlex2,
			"Flex10": self._Flex10,
			"ScaleFlex2": self._ScaleFlex2,
			"Anchor2": self._Anchor2,
			"FramerFlex3": self._FramerFlex3,
			"TextBox11": self._TextBox11,
			"TextBox12": self._TextBox12,
			"TextBox13": self._TextBox13,
			"TextBox14": self._TextBox14,
			"Image3": self._Image3,
			"Flex11": self._Flex11,
			"ButtonFlex3": self._ButtonFlex3,
			"Flex12": self._Flex12,
			"ScaleFlex3": self._ScaleFlex3,
			"Anchor3": self._Anchor3,
			"FramerFlex4": self._FramerFlex4,
			"TextBox15": self._TextBox15,
			"TextBox16": self._TextBox16,
			"TextBox17": self._TextBox17,
			"TextBox18": self._TextBox18,
			"Image4": self._Image4,
			"Flex13": self._Flex13,
			"ButtonFlex4": self._ButtonFlex4,
			"Flex14": self._Flex14,
			"ScaleFlex4": self._ScaleFlex4,
			"Anchor4": self._Anchor4,
			"FramerFlex5": self._FramerFlex5,
			"TextBox19": self._TextBox19,
			"TextBox20": self._TextBox20,
			"TextBox21": self._TextBox21,
			"TextBox22": self._TextBox22,
			"Image5": self._Image5,
			"Flex15": self._Flex15,
			"ButtonFlex5": self._ButtonFlex5,
			"Flex16": self._Flex16,
			"ScaleFlex5": self._ScaleFlex5,
			"Anchor5": self._Anchor5,
			"FramerFlex6": self._FramerFlex6,
			"TextBox23": self._TextBox23,
			"TextBox24": self._TextBox24,
			"TextBox25": self._TextBox25,
			"TextBox26": self._TextBox26,
			"Image6": self._Image6,
			"Flex17": self._Flex17,
			"ButtonFlex6": self._ButtonFlex6,
			"Flex18": self._Flex18,
			"ScaleFlex6": self._ScaleFlex6,
			"Anchor6": self._Anchor6,
			"FramerFlex7": self._FramerFlex7,
			"Flex19": self._Flex19,
			"Flex20": self._Flex20,
			"FramerFlex8": self._FramerFlex8,
			"Flex21": self._Flex21,
			"Flex22": self._Flex22,
			"Div1": self._Div1,
			"TextBox27": self._TextBox27,
			"Anchor7": self._Anchor7,
			"Flex23": self._Flex23,
			"TextBox28": self._TextBox28,
			"FramerText1": self._FramerText1,
			"FramerText2": self._FramerText2,
			"TextBox30": self._TextBox30,
			"Anchor8": self._Anchor8,
			"Flex24": self._Flex24
			}
  