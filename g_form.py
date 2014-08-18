import sublime, sublime_plugin
import re

def match(rex, str):
    m = rex.match(str)
    if m:
        return m.group(0)
    else:
        return None


# Provide completions that match just after typing an opening angle bracket
class TagCompletionss(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        # Only trigger within JavaScript
        if not view.match_selector(locations[0],
                "source.js"):
            return []

        pt = locations[0] - len(prefix) - 7
        ch = view.substr(sublime.Region(pt, pt + 7))
        if ch != 'g_user.':
            return []

        return ([
                ("userName();","userName();"),
                ("firstName();", "firstName();"),
                ("lastName();", "lastName();"),
                ("fullName();", "fullName();"),
                ("roles();", "roles();"),
                ("userID();", "userID();"),
                ("preferences();", "preferences();"),
                ("clientData();", "clientData();"),
                ("initialize(userName, firstName, lastName, commaRoles, userID);", "initialize(${10:userName}, ${20:firstName}, ${30:lastName}, ${40:commaRoles}, ${50:userID});"),
                ("hasRoleExactly(role);", "hasRoleExactly(${10:role});"),
                ("hasRoles();", "hasRoles();"),
                ("hasRole(role);", "hasRole(${10:role});"),
                ("hasRoleFromList(roles);", "hasRoleFromList(${10:roles});"),
                ("getFullName();", "getFullName();"),
                ("getUserName();", "getUserName();"),
                ("getUserID();", "getUserID();"),
                ("setFullName(fn);", "setFullName(${10:fn});"),
                ("getRoles();", "getRoles();"),
                ("getAvailableElevatedRoles();", "getAvailableElevatedRoles();"),
                ("setRoles(r);", "setRoles(${10:r});"),
                ("setElevatedRoles(r);", "setElevatedRoles(${10:r});"),
                ("setActiveElevatedRoles(r);", "setActiveElevatedRoles(${10:r});"),
                ("getActiveElevatedRoles();", "getActiveElevatedRoles();"),
                ("getPreference(n);", "getPreference(${10:n});"),
                ("setPreference(n, v);", "setPreference(${10:n}, ${20:v});"),
                ("deletePreference(n);", "deletePreference(${10:n});"),
                ("getClientData(n);", "getClientData(${10:n});"),
                ("setClientData(n, v);", "setClientData(${10:n}, ${20:v});"),
                ("setBannerImage(s);", "setBannerImage(${10:s});"),
                ("getBannerImage();", "getBannerImage();"),
                ("setBannerText(s);", "setBannerText(${10:s});"),
                ("getBannerText();", "getBannerText();"),
                ("setHomePages(s);", "setHomePages(${10:s});"),
                ("getHomePages();", "getHomePages();"),
                ("type();", "type();")

              ], sublime.INHIBIT_WORD_COMPLETIONS | sublime.INHIBIT_EXPLICIT_COMPLETIONS)
