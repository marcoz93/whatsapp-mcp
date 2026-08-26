package main

import (
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strings"
)

var profileNamePattern = regexp.MustCompile(`^[a-z0-9][a-z0-9_-]*$`)

type AccountProfile struct {
	Name     string
	StoreDir string
}

type AccountIdentity struct {
	Profile      string `json:"profile"`
	JID          string `json:"jid"`
	PushName     string `json:"push_name"`
	BusinessName string `json:"business_name"`
}

func loadActiveProfile(bridgeDir string) (AccountProfile, error) {
	raw, err := os.ReadFile(filepath.Join(bridgeDir, ".active-profile"))
	if err != nil {
		return AccountProfile{}, fmt.Errorf("read active profile: %w", err)
	}

	name := strings.TrimSpace(string(raw))
	if !profileNamePattern.MatchString(name) {
		return AccountProfile{}, fmt.Errorf("invalid active profile %q", name)
	}

	storeDir, err := filepath.Abs(filepath.Join(bridgeDir, "profiles", name))
	if err != nil {
		return AccountProfile{}, fmt.Errorf("resolve profile path: %w", err)
	}
	info, err := os.Stat(storeDir)
	if err != nil {
		return AccountProfile{}, fmt.Errorf("open profile %q: %w", name, err)
	}
	if !info.IsDir() {
		return AccountProfile{}, fmt.Errorf("profile path is not a directory: %s", name)
	}

	return AccountProfile{Name: name, StoreDir: storeDir}, nil
}

func (profile AccountProfile) SessionDB() string {
	return filepath.Join(profile.StoreDir, "whatsapp.db")
}

func (profile AccountProfile) MessagesDB() string {
	return filepath.Join(profile.StoreDir, "messages.db")
}

func mediaDirectory(storeDir, chatJID string) string {
	return filepath.Join(storeDir, strings.ReplaceAll(chatJID, ":", "_"))
}

func validateExpectedProfile(expected, active string) error {
	if expected == "" {
		return fmt.Errorf("expected_profile is required; active profile is %q", active)
	}
	if expected != active {
		return fmt.Errorf("expected profile %q, active profile is %q", expected, active)
	}
	return nil
}

func newAccountIdentity(profile, jid, pushName, businessName string) AccountIdentity {
	return AccountIdentity{
		Profile:      profile,
		JID:          jid,
		PushName:     pushName,
		BusinessName: businessName,
	}
}
