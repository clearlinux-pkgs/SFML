#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : SFML
Version  : 2.5.1.s
Release  : 5
URL      : https://www.sfml-dev.org/files/SFML-2.5.1-sources.zip
Source0  : https://www.sfml-dev.org/files/SFML-2.5.1-sources.zip
Summary  : The Simple and Fast Multimedia Library, window module.
Group    : Development/Tools
License  : Zlib
Requires: SFML-data = %{version}-%{release}
Requires: SFML-lib = %{version}-%{release}
Requires: SFML-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : doxygen
BuildRequires : extra-cmake-modules pkgconfig(egl)
BuildRequires : flac-dev
BuildRequires : freetype-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : libvorbis-dev
BuildRequires : mesa-dev
BuildRequires : openal-soft-dev
BuildRequires : systemd-dev

%description
[![SFML logo](https://www.sfml-dev.org/images/logo.png)](https://www.sfml-dev.org)

%package data
Summary: data components for the SFML package.
Group: Data

%description data
data components for the SFML package.


%package dev
Summary: dev components for the SFML package.
Group: Development
Requires: SFML-lib = %{version}-%{release}
Requires: SFML-data = %{version}-%{release}
Provides: SFML-devel = %{version}-%{release}
Requires: SFML = %{version}-%{release}

%description dev
dev components for the SFML package.


%package lib
Summary: lib components for the SFML package.
Group: Libraries
Requires: SFML-data = %{version}-%{release}
Requires: SFML-license = %{version}-%{release}

%description lib
lib components for the SFML package.


%package license
Summary: license components for the SFML package.
Group: Default

%description license
license components for the SFML package.


%prep
%setup -q -n SFML-2.5.1
cd %{_builddir}/SFML-2.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604603384
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604603384
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SFML
cp %{_builddir}/SFML-2.5.1/license.md %{buildroot}/usr/share/package-licenses/SFML/d25b34e8485ae2cf7de4fc5a0c5a9425898bdff9
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/SFML/license.md
/usr/share/SFML/readme.md

%files dev
%defattr(-,root,root,-)
/usr/include/SFML/Audio.hpp
/usr/include/SFML/Audio/AlResource.hpp
/usr/include/SFML/Audio/Export.hpp
/usr/include/SFML/Audio/InputSoundFile.hpp
/usr/include/SFML/Audio/Listener.hpp
/usr/include/SFML/Audio/Music.hpp
/usr/include/SFML/Audio/OutputSoundFile.hpp
/usr/include/SFML/Audio/Sound.hpp
/usr/include/SFML/Audio/SoundBuffer.hpp
/usr/include/SFML/Audio/SoundBufferRecorder.hpp
/usr/include/SFML/Audio/SoundFileFactory.hpp
/usr/include/SFML/Audio/SoundFileFactory.inl
/usr/include/SFML/Audio/SoundFileReader.hpp
/usr/include/SFML/Audio/SoundFileWriter.hpp
/usr/include/SFML/Audio/SoundRecorder.hpp
/usr/include/SFML/Audio/SoundSource.hpp
/usr/include/SFML/Audio/SoundStream.hpp
/usr/include/SFML/Config.hpp
/usr/include/SFML/GpuPreference.hpp
/usr/include/SFML/Graphics.hpp
/usr/include/SFML/Graphics/BlendMode.hpp
/usr/include/SFML/Graphics/CircleShape.hpp
/usr/include/SFML/Graphics/Color.hpp
/usr/include/SFML/Graphics/ConvexShape.hpp
/usr/include/SFML/Graphics/Drawable.hpp
/usr/include/SFML/Graphics/Export.hpp
/usr/include/SFML/Graphics/Font.hpp
/usr/include/SFML/Graphics/Glsl.hpp
/usr/include/SFML/Graphics/Glsl.inl
/usr/include/SFML/Graphics/Glyph.hpp
/usr/include/SFML/Graphics/Image.hpp
/usr/include/SFML/Graphics/PrimitiveType.hpp
/usr/include/SFML/Graphics/Rect.hpp
/usr/include/SFML/Graphics/Rect.inl
/usr/include/SFML/Graphics/RectangleShape.hpp
/usr/include/SFML/Graphics/RenderStates.hpp
/usr/include/SFML/Graphics/RenderTarget.hpp
/usr/include/SFML/Graphics/RenderTexture.hpp
/usr/include/SFML/Graphics/RenderWindow.hpp
/usr/include/SFML/Graphics/Shader.hpp
/usr/include/SFML/Graphics/Shape.hpp
/usr/include/SFML/Graphics/Sprite.hpp
/usr/include/SFML/Graphics/Text.hpp
/usr/include/SFML/Graphics/Texture.hpp
/usr/include/SFML/Graphics/Transform.hpp
/usr/include/SFML/Graphics/Transformable.hpp
/usr/include/SFML/Graphics/Vertex.hpp
/usr/include/SFML/Graphics/VertexArray.hpp
/usr/include/SFML/Graphics/VertexBuffer.hpp
/usr/include/SFML/Graphics/View.hpp
/usr/include/SFML/Main.hpp
/usr/include/SFML/Network.hpp
/usr/include/SFML/Network/Export.hpp
/usr/include/SFML/Network/Ftp.hpp
/usr/include/SFML/Network/Http.hpp
/usr/include/SFML/Network/IpAddress.hpp
/usr/include/SFML/Network/Packet.hpp
/usr/include/SFML/Network/Socket.hpp
/usr/include/SFML/Network/SocketHandle.hpp
/usr/include/SFML/Network/SocketSelector.hpp
/usr/include/SFML/Network/TcpListener.hpp
/usr/include/SFML/Network/TcpSocket.hpp
/usr/include/SFML/Network/UdpSocket.hpp
/usr/include/SFML/OpenGL.hpp
/usr/include/SFML/System.hpp
/usr/include/SFML/System/Clock.hpp
/usr/include/SFML/System/Err.hpp
/usr/include/SFML/System/Export.hpp
/usr/include/SFML/System/FileInputStream.hpp
/usr/include/SFML/System/InputStream.hpp
/usr/include/SFML/System/Lock.hpp
/usr/include/SFML/System/MemoryInputStream.hpp
/usr/include/SFML/System/Mutex.hpp
/usr/include/SFML/System/NativeActivity.hpp
/usr/include/SFML/System/NonCopyable.hpp
/usr/include/SFML/System/Sleep.hpp
/usr/include/SFML/System/String.hpp
/usr/include/SFML/System/String.inl
/usr/include/SFML/System/Thread.hpp
/usr/include/SFML/System/Thread.inl
/usr/include/SFML/System/ThreadLocal.hpp
/usr/include/SFML/System/ThreadLocalPtr.hpp
/usr/include/SFML/System/ThreadLocalPtr.inl
/usr/include/SFML/System/Time.hpp
/usr/include/SFML/System/Utf.hpp
/usr/include/SFML/System/Utf.inl
/usr/include/SFML/System/Vector2.hpp
/usr/include/SFML/System/Vector2.inl
/usr/include/SFML/System/Vector3.hpp
/usr/include/SFML/System/Vector3.inl
/usr/include/SFML/Window.hpp
/usr/include/SFML/Window/Clipboard.hpp
/usr/include/SFML/Window/Context.hpp
/usr/include/SFML/Window/ContextSettings.hpp
/usr/include/SFML/Window/Cursor.hpp
/usr/include/SFML/Window/Event.hpp
/usr/include/SFML/Window/Export.hpp
/usr/include/SFML/Window/GlResource.hpp
/usr/include/SFML/Window/Joystick.hpp
/usr/include/SFML/Window/Keyboard.hpp
/usr/include/SFML/Window/Mouse.hpp
/usr/include/SFML/Window/Sensor.hpp
/usr/include/SFML/Window/Touch.hpp
/usr/include/SFML/Window/VideoMode.hpp
/usr/include/SFML/Window/Window.hpp
/usr/include/SFML/Window/WindowHandle.hpp
/usr/include/SFML/Window/WindowStyle.hpp
/usr/lib64/cmake/SFML/SFMLConfig.cmake
/usr/lib64/cmake/SFML/SFMLConfigDependencies.cmake
/usr/lib64/cmake/SFML/SFMLConfigVersion.cmake
/usr/lib64/cmake/SFML/SFMLSharedTargets-relwithdebinfo.cmake
/usr/lib64/cmake/SFML/SFMLSharedTargets.cmake
/usr/lib64/libsfml-audio.so
/usr/lib64/libsfml-graphics.so
/usr/lib64/libsfml-network.so
/usr/lib64/libsfml-system.so
/usr/lib64/libsfml-window.so
/usr/lib64/pkgconfig/sfml-all.pc
/usr/lib64/pkgconfig/sfml-audio.pc
/usr/lib64/pkgconfig/sfml-graphics.pc
/usr/lib64/pkgconfig/sfml-network.pc
/usr/lib64/pkgconfig/sfml-system.pc
/usr/lib64/pkgconfig/sfml-window.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsfml-audio.so.2.5
/usr/lib64/libsfml-audio.so.2.5.1
/usr/lib64/libsfml-graphics.so.2.5
/usr/lib64/libsfml-graphics.so.2.5.1
/usr/lib64/libsfml-network.so.2.5
/usr/lib64/libsfml-network.so.2.5.1
/usr/lib64/libsfml-system.so.2.5
/usr/lib64/libsfml-system.so.2.5.1
/usr/lib64/libsfml-window.so.2.5
/usr/lib64/libsfml-window.so.2.5.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SFML/d25b34e8485ae2cf7de4fc5a0c5a9425898bdff9
