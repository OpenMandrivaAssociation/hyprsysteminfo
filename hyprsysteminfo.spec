Name:     hyprsysteminfo
Version:	0.2.0
Release:	2
Summary:	System info utility for Hyprland
License:	BSD-3-Clause
Group:		Hyprland

URL:		https://github.com/hyprwm/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:	cmake
BuildOption:	-DCMAKE_BUILD_TYPE=Release

BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(pixman-1)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(aquamarine)
BuildRequires: pkgconfig(hyprutils) >= 0.10.2
BuildRequires: pkgconfig(hyprtoolkit)
BuildRequires: pkgconfig(hyprgraphics)
BuildRequires: vulkan-headers
BuildRequires: glaze-devel


Requires: /usr/bin/lscpu
Requires: /usr/bin/lspci
Requires: /usr/bin/free

%description
%{summary}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
