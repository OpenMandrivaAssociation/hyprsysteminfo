Name:     hyprsysteminfo
Version:	0.1.3
Release:	6
Summary:	A tiny qt6/wml application to display information about the running system
License:	BSD-3-Clause
Group:		Hyprland

URL:		https://github.com/hyprwm/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		https://github.com/hyprwm/hyprsysteminfo/pull/21.patch
BuildSystem:	cmake

BuildRequires: desktop-file-utils
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WaylandClient)
BuildRequires: qt6-qtbase-tools
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(hyprutils)

Requires: /usr/bin/lscpu
Requires: /usr/bin/lspci
Requires: /usr/bin/free
Requires: hyprland-qt-support

%description
%{summary}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
