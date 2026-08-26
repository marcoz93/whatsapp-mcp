package main

import (
	"os"
	"path/filepath"
	"testing"
)

func TestLoadActiveProfile(t *testing.T) {
	bridgeDir := t.TempDir()
	storeDir := filepath.Join(bridgeDir, "profiles", "empresa")
	if err := os.MkdirAll(storeDir, 0700); err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(
		filepath.Join(bridgeDir, ".active-profile"),
		[]byte("empresa\n"),
		0600,
	); err != nil {
		t.Fatal(err)
	}

	profile, err := loadActiveProfile(bridgeDir)
	if err != nil {
		t.Fatal(err)
	}
	if profile.Name != "empresa" {
		t.Fatalf("profile name = %q, want empresa", profile.Name)
	}
	if profile.StoreDir != storeDir {
		t.Fatalf("store dir = %q, want %q", profile.StoreDir, storeDir)
	}
	if profile.SessionDB() != filepath.Join(storeDir, "whatsapp.db") {
		t.Fatalf("unexpected session database: %s", profile.SessionDB())
	}
	if profile.MessagesDB() != filepath.Join(storeDir, "messages.db") {
		t.Fatalf("unexpected messages database: %s", profile.MessagesDB())
	}
}

func TestLoadActiveProfileRejectsTraversal(t *testing.T) {
	bridgeDir := t.TempDir()
	if err := os.WriteFile(
		filepath.Join(bridgeDir, ".active-profile"),
		[]byte("../empresa\n"),
		0600,
	); err != nil {
		t.Fatal(err)
	}

	if _, err := loadActiveProfile(bridgeDir); err == nil {
		t.Fatal("expected invalid profile error")
	}
}

func TestLoadActiveProfileRequiresExistingDirectory(t *testing.T) {
	bridgeDir := t.TempDir()
	if err := os.WriteFile(
		filepath.Join(bridgeDir, ".active-profile"),
		[]byte("pessoal\n"),
		0600,
	); err != nil {
		t.Fatal(err)
	}

	if _, err := loadActiveProfile(bridgeDir); err == nil {
		t.Fatal("expected missing profile directory error")
	}
}

func TestNewMessageStoreUsesProfileDirectory(t *testing.T) {
	storeDir := t.TempDir()
	store, err := NewMessageStore(storeDir)
	if err != nil {
		t.Fatal(err)
	}
	defer store.Close()

	if store.storeDir != storeDir {
		t.Fatalf("store dir = %q, want %q", store.storeDir, storeDir)
	}
	if _, err := os.Stat(filepath.Join(storeDir, "messages.db")); err != nil {
		t.Fatalf("messages database was not created in profile: %v", err)
	}
}

func TestMediaDirectoryUsesProfileDirectory(t *testing.T) {
	storeDir := filepath.Join(t.TempDir(), "profiles", "empresa")
	got := mediaDirectory(storeDir, "123:45@g.us")
	want := filepath.Join(storeDir, "123_45@g.us")
	if got != want {
		t.Fatalf("media directory = %q, want %q", got, want)
	}
}
