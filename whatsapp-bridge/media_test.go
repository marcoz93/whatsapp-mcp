package main

import (
	"os"
	"path/filepath"
	"testing"
)

func TestMediaDownloadPreservesSignatureAndMessageIdentity(t *testing.T) {
	const directPath = "/v/example.enc?ccb=11-4&oh=signed%2Bvalue&oe=expiry"
	for _, input := range []string{"https://mmg.whatsapp.net" + directPath, directPath} {
		if got := extractDirectPathFromURL(input); got != directPath {
			t.Fatalf("direct path = %q, want %q", got, directPath)
		}
	}

	store, err := NewMessageStore(t.TempDir())
	if err != nil {
		t.Fatal(err)
	}
	defer store.Close()
	const chat = "example@g.us"
	if _, err = store.db.Exec("INSERT INTO chats (jid) VALUES (?)", chat); err != nil {
		t.Fatal(err)
	}
	dir := mediaDirectory(store.storeDir, chat)
	if err = os.MkdirAll(dir, 0700); err != nil {
		t.Fatal(err)
	}
	for _, id := range []string{"message1", "message2"} {
		if _, err = store.db.Exec("INSERT INTO messages (id, chat_jid, media_type, filename) VALUES (?, ?, 'image', 'same-second.jpg')", id, chat); err != nil {
			t.Fatal(err)
		}
		want := filepath.Join(dir, id+"_same-second.jpg")
		if err = os.WriteFile(want, []byte(id), 0600); err != nil {
			t.Fatal(err)
		}
		ok, _, _, got, err := downloadMedia(nil, store, id, chat)
		if err != nil || !ok || got != want {
			t.Fatalf("download %s = %q, %v, %v; want %q", id, got, ok, err, want)
		}
	}
}
