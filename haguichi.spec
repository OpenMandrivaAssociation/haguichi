Name:           haguchi
Version:        1.4.1
Release:        1
Summary:        Hamachi Network Manager
License:        GPLv3+
Group:          Productivity/Networking/Other
URL:            https://www.haguichi.net/
Source0:        https://launchpad.net/haguichi/1.4/%{version}/+download/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libnotify)
Recommends:     %{name}-lang
