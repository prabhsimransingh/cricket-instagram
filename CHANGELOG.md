# Changelog

All notable changes to WicketGram will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [v12] - 2025-06-21

### Added
- Intelligent Match Form with team-based score breakdown
- Victory dropdown ("Which Team Won?") for explicit result selection
- Auto-calculated margin calculation (runs difference for wins, wickets remaining for losses)
- Team A and Team B sections with separate Score, Wickets Lost, and Overs Faced fields
- Contextual motivational messaging in AI prompts (celebratory for wins, resilient for losses)
- Full score display (e.g., "156/5") calculated from runs and wickets
- Enhanced buildPrompt_match() with victory context
- Sample data updated with new intelligent form fields

### Changed
- Match form layout redesigned with clear team sections
- AI prompts now include victory-specific language and tone
- Margin calculation moved from manual input to automatic

### Fixed
- No regressions in other post types
- All existing features preserved

---

## [v11] - 2025-06-20

### Added
- Instagram button Option 1: Copy image to clipboard before opening app
- Proper toast notifications for clipboard copy success/failure
- Instruction toast showing "Paste image in Instagram (Cmd+V or Ctrl+V)"
- Desktop fallback: shows instruction message without opening app

### Changed
- shareToInstagramApp() now copies image to clipboard first
- Platform detection improved (Android, iOS, Desktop)

### Fixed
- Instagram button now passes image along with app opening
- Clipboard copy error handling with user-friendly messages

---

## [v10] - 2025-06-19

### Added
- AI preview sections for all 6 post types:
  - Match (ai-preview-img-match)
  - Fixture (ai-preview-img)
  - Squad (ai-preview-img-squad)
  - MOTM (ai-preview-img-motm)
  - Milestone (ai-preview-img-milestone)
  - Photo (ai-preview-img-photo)
- Unified action buttons across all post types (Share, Instagram App, Copy, Regenerate)

### Fixed
- Critical bug: AI images now appear in the correct tab where user clicked "Enhance with AI"
- Previously images only showed in Fixture tab regardless of selected post type

---

## [v9] - 2025-06-18

### Added
- Enhanced AI prompts that capture ALL form data
- All 6 prompt builders now include complete field usage:
  - buildPrompt_match(): date, margin, top batter stats, top bowler stats
  - buildPrompt_fixture(): datetime included
  - buildPrompt_squad(): complete player list
  - buildPrompt_motm(): date, strike rate, fielding contributions
  - buildPrompt_milestone(): subtitle included
  - buildPrompt_photo(): caption included

### Changed
- More comprehensive AI image generation with complete context
- Console logging showing captured data and generated prompts for debugging

### Fixed
- v9 added to version whitelist for ?version=v9 testing

---

## [v8] - 2025-06-17

### Added
- AI preview image persistence across page refreshes using localStorage
- localStorage save in generateAICardForType()
- localStorage restore in init() function
- Console logging for AI preview state tracking

### Changed
- AI preview now survives page refresh (stored in localStorage)

### Fixed
- AI images disappearing on page refresh

---

## [v7] - 2025-06-16

### Added
- Version system with ?version=vX URL parameters
- Version whitelist for selective version testing
- Meta tags to prevent caching issues

### Changed
- Multiple versions accessible via URL parameter
- Easier A/B testing and rollback capability

---

## [v6] - 2025-06-15

### Added
- Clipboard copy functionality (copyImage, copyCaption)
- Toast notifications for copy success/failure
- Image blob handling for clipboard API

### Changed
- "Add to Queue" button replaced with clipboard buttons
- Direct copy-to-clipboard workflow

---

## [v5] - 2025-06-14

### Added
- Canvas-based card rendering for all 6 post types
- Real-time preview with debouncedPreview()
- Card customization (colors, logos, text)

### Changed
- Unified rendering pipeline for all post types

---

## [v4] - 2025-06-13

### Added
- AI caption generation via Groq API
- 3 caption options for each post
- Caption selection UI with card styling

### Changed
- Caption generation integrated with post creation

---

## [v3] - 2025-06-12

### Added
- AI image generation via DALL-E 3 and Pollinations.ai
- "Enhance with AI" button for each post type
- AI preview section with image display

### Changed
- Manual image upload → AI-generated images
- Enhanced user experience with AI features

---

## [v2] - 2025-06-11

### Added
- Queue management system (draft, approve, post, history)
- Post approval workflow
- History tracking of posted content
- Settings tab for API key configuration
- Club customization (name, colors, logos)

### Changed
- Multi-tab interface (Queue, History, New Post, Settings)
- localStorage persistence for all data

---

## [v1] - 2025-06-10

### Added
- Initial release: Gabru Jawaans cricket Instagram dashboard
- 6 post types: Match Result, Fixture, Squad, MOTM, Milestone, Photo
- Form-based post creation
- Canvas-based card preview
- Basic Ayrshare integration for Instagram posting
- localStorage for client-side persistence
- Settings tab for API key management
- Responsive design (mobile, tablet, desktop)

### Features
- Alpine.js reactive UI
- Tailwind CSS styling
- Canvas API for card rendering
- Form validation
- Toast notifications
- Real-time preview

---

## Future Roadmap

### Planned Features
- [ ] TikTok post type (9:16 format with trending sounds)
- [ ] Facebook variant (1.91:1 aspect ratio)
- [ ] Batch posting & scheduling
- [ ] Analytics dashboard
- [ ] Android app (React Native)
- [ ] iOS app
- [ ] Video post support
- [ ] Community gallery
- [ ] Dark mode
- [ ] Multiple club profiles

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to WicketGram.

## Support

For issues, feature requests, or questions, please open an [Issue](https://github.com/prabhsimransingh/cricket-instagram/issues) or start a [Discussion](https://github.com/prabhsimransingh/cricket-instagram/discussions).
