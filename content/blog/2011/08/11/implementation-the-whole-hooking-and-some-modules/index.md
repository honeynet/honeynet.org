---
title: "Implementation: the whole hooking and some modules"
date: "2011-08-11"
---

The whole implementation is mainly consisted of 4 modules: central controller, emulator, dummy control and list. Central controller is a dynamic link library written in C++. Emulator and dummy control are COM components written in python and registered into registry by win32com.server.register.UseCommandLine. List is a text file in a certain format to read and modify.  
The implementation considers the further updating for new controls’ emulation. One need only modified the emulating, existing of available list and adding new methods into emulator. The Central controller needs not to do any change. Below is the description for each module.  
  
1 Central controller  
  
Central controller is made up of hook manager, hook info, system API hooked methods and interface hooked methods. The hooked methods are shown below.  
  
Original Type  
CLSIDFromProgID System API  
CoCreateInstanceEx System API  
CoGetClassObject System API  
IClassFactory::QueryInterface Interface of IClassFactory  
IClassFactory::Release Interface of IClassFactory  
IClassFactory::CreateInstance Interface of IClassFactory  
IDispatch::QueryInterface Interface of IDispatch  
IDispatch::Release Interface of IDispatch  
IDispatch::GetIDsOfNames Interface of IDispatch  
IDispatch::Invoke Interface of IDispatch  
IDispatchEx::GetDispID Interface of IDispatchEx  
IDispatchEx::InvokeEx Interface of IDispatchEx  
IDispatchEx::Release Interface of IDispatchEx  
  
The hooked system API calls original method to create a new instance, and injects code into IClassFactory’s and IDispatch/IDispatchEx’s virtual tables. If client calls for CLSIDFromProgID method to obtain GUID of control, hooker logs this calling and invokes original CLSIDFromProgID. For instance, the Download.DLoader instance is created by tag indicated below:  
  
  
The formal creation should be  
a) calling CoGetClassObject to get Download.DLoader Class Factory object.  
b) calling IClassFActory::CreateInstance to create Download.DLoader object.  
  
After hooking, the process should be:  
a) Client calls CoGetClassObject, but hooked by HookCoGetClassObject  
b) HookCoGetClassObject logs and invokes CoGetClassObject, which produces class factory object  
c) The class factory is hooked by hook manager once created.  
d) Class Factory’s CreateInstance method will be invoked but linked to HookCreateInstance. This method logs the invocation, calls original CreateInstance and injects code into IDispatch(in situation of creation, the interface is IDispatch while for javascript creation, the interface will be IDispatchEx which inherited from IDispatch).  
  
To call function, client uses IDispatch/IDispathEx interface to get method address. The hooked method triggers hook manager to find the original method, which stored into an interface virtual table-hook info class map before injection. The hook info class stores interface address. After getting method address, the hooked method takes advantage of interface to invoke method in emulator. The process ends with emulator’s returning.  
  
For instance, to sentence install\["DownloadAndInstall"\](YEtYcJsR1), the process for the actual invocation should be:  
a) IDispatch -> vtbl -> GetIDofNames method is called with argument of method name, which is string “install” in our sample. This returns the interface for “install” method  
b) Client calls IDispatch ->vtbl -> Invoke with parameter that we obtained from GetIDofNames to invoke responding method.  
  
After hooking, the process should be:  
a) GetIDofNames method is hooked to HookGetIDofNames, which transfers the name in control to the one in emulator by consulting into map.  
b) HookGetIDofNames get value from emulator’s GetIDofNames with argument of name string.  
c) Client call IDispatch -> vtbl -> Invoke method, with the returning value from HookGetIDofNames. Because the value is actually the method in emulator, this invocation will call emulator’s responding method.  
  
2 Emulator  
  
The method names’ conversion is according to the following approach: connecting the respective string of control and the emulating method, i.e. DownloaderDLoaderDownloadAndInstall for DownloadAndInstall function of Downloader.DLoader object.  
The method is actually checking the argument to detect malicious behavior. Meanwhile, it returns true as result of an invocation.  
  
3 Dummy control  
  
We consider its implementation by python language, for python is more convenient and easier to handle. The code is shown below. For further development, we will build up a automatic dummy control register. This tool can read the emulating and existing list, extract program ID and class ID, and register all controls needed into registry.  
  
class Dummy:  
\_public\_methods\_ = \[\]  
\_reg\_progid\_ = "Downloader.DLoader"  
\_reg\_clsid\_ = "{78ABDC59-D8E7-44D3-9A76-9A0918C52B4A}"  
if \_\_name\_\_=='\_\_main\_\_':  
import win32com.server.register  
win32com.server.register.UseCommandLine(Dummy)  
  
4 List  
  
To specify each strategy, we define three lists: emulating list, existing list and available list. All the list obeys “EmulatorProgid {ClassID} ProgramID” format. To controls with same class ID but different program ID, each program ID will occupy one line. For instance, if we aim to emulate the Downloader.DLoader control, we add the information in such a format:  
DownloaderDLoader {78ABDC59-D8E7-44D3-9A76-9A0918C52B4A} Downloader.DLoader
