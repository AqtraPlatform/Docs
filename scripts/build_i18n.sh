#!/bin/bash
# Скрипт для сборки многоязычной документации

set -e

echo "🌍 Сборка многоязычной документации Aqtra Docs"

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Функция для вывода сообщений
log() {
    echo -e "${BLUE}[$(date +'%Y-%m-%d %H:%M:%S')]${NC} $1"
}

success() {
    echo -e "${GREEN}✅ $1${NC}"
}

warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

error() {
    echo -e "${RED}❌ $1${NC}"
}

# Проверяем наличие Poetry
if ! command -v poetry &> /dev/null; then
    error "Poetry не найден. Установите Poetry для продолжения."
    exit 1
fi

# Переходим в директорию проекта
cd "$(dirname "$0")/.."

log "Установка зависимостей..."
poetry install

log "Генерация английской версии документации..."
poetry run python tools/po_to_md.py --lang en --allow-fuzzy

if [ $? -eq 0 ]; then
    success "Английская версия сгенерирована успешно"
else
    error "Ошибка при генерации английской версии"
    exit 1
fi

log "Сборка документации..."
poetry run mkdocs build

if [ $? -eq 0 ]; then
    success "Документация собрана успешно"
else
    error "Ошибка при сборке документации"
    exit 1
fi

log "Запуск локального сервера..."
echo ""
echo "🌐 Документация доступна по адресам:"
echo "   🇷🇺 Русская версия: http://127.0.0.1:8080/"
echo "   🇬🇧 English version: http://127.0.0.1:8080/en/"
echo ""
echo "Для остановки сервера нажмите Ctrl+C"
echo ""

poetry run mkdocs serve --dev-addr=127.0.0.1:8080
