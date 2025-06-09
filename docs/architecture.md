# 공학용 계산기 웹앱 아키텍처 설계

## 1. 아키텍처 개요

### 1.1 아키텍처 패턴
- Clean Architecture 기반 설계
- MVVM (Model-View-ViewModel) 패턴 적용
- Provider를 통한 상태 관리

### 1.2 기술 스택
- Flutter Web
- Dart
- Provider (상태 관리)
- math_expressions (수학 표현식 처리)
- flutter_calculator_keypad (UI 컴포넌트)

## 2. 레이어 구조

### 2.1 Presentation Layer
```
lib/
├── presentation/
│   ├── screens/
│   │   ├── calculator_screen.dart
│   │   └── history_screen.dart
│   ├── widgets/
│   │   ├── calculator_keypad.dart
│   │   ├── display_panel.dart
│   │   ├── history_panel.dart
│   │   └── theme_switcher.dart
│   └── viewmodels/
│       ├── calculator_viewmodel.dart
│       └── history_viewmodel.dart
```

### 2.2 Domain Layer
```
lib/
├── domain/
│   ├── models/
│   │   ├── calculation.dart
│   │   └── history_item.dart
│   ├── repositories/
│   │   └── calculation_repository.dart
│   └── usecases/
│       ├── calculate_expression.dart
│       ├── save_to_history.dart
│       └── get_history.dart
```

### 2.3 Data Layer
```
lib/
├── data/
│   ├── repositories/
│   │   └── calculation_repository_impl.dart
│   └── storage/
│       └── local_storage.dart
```

## 3. 컴포넌트 상세 설계

### 3.1 Presentation Layer
#### 3.1.1 Screens
- `CalculatorScreen`: 메인 계산기 화면
  - 계산기 키패드
  - 결과 표시 패널
  - 모드 전환 버튼
  - 테마 전환 버튼

- `HistoryScreen`: 계산 이력 화면
  - 이력 목록
  - 이력 재사용 기능
  - 이력 삭제 기능

#### 3.1.2 ViewModels
- `CalculatorViewModel`
  - 수식 입력 처리
  - 계산 실행
  - 결과 표시
  - 모드 전환

- `HistoryViewModel`
  - 이력 관리
  - 이력 저장
  - 이력 불러오기

### 3.2 Domain Layer
#### 3.2.1 Models
- `Calculation`
  - 수식
  - 결과
  - 타임스탬프

- `HistoryItem`
  - 계산 기록
  - 메타데이터

#### 3.2.2 UseCases
- `CalculateExpression`
  - 수식 유효성 검사
  - 계산 실행
  - 결과 포맷팅

- `SaveToHistory`
  - 계산 결과 저장
  - 이력 관리

### 3.3 Data Layer
#### 3.3.1 Storage
- `LocalStorage`
  - 계산 이력 저장
  - 세션 데이터 관리
  - 테마 설정 저장

## 4. 데이터 흐름

### 4.1 계산 프로세스
1. 사용자 입력 → CalculatorScreen
2. CalculatorViewModel에서 입력 처리
3. CalculateExpression UseCase 호출
4. 계산 결과 반환
5. 결과 표시 및 이력 저장

### 4.2 이력 관리 프로세스
1. 계산 완료 → SaveToHistory UseCase
2. LocalStorage에 저장
3. HistoryViewModel에서 이력 관리
4. HistoryScreen에 표시

## 5. 상태 관리

### 5.1 Provider 구조
```
lib/
├── providers/
│   ├── calculator_provider.dart
│   ├── history_provider.dart
│   └── theme_provider.dart
```

### 5.2 상태 객체
- `CalculatorState`
  - 현재 수식
  - 계산 결과
  - 입력 모드
  - 에러 상태

- `HistoryState`
  - 이력 목록
  - 선택된 이력
  - 필터 상태

## 6. 테마 관리

### 6.1 테마 구조
```
lib/
├── theme/
│   ├── app_theme.dart
│   ├── light_theme.dart
│   └── dark_theme.dart
```

### 6.2 테마 전환
- 시스템 테마 감지
- 수동 테마 전환
- 테마 설정 저장

## 7. 에러 처리

### 7.1 에러 타입
- 수식 오류
- 계산 오류
- 저장 오류

### 7.2 에러 처리 방식
- 사용자 친화적 에러 메시지
- 에러 로깅
- 복구 메커니즘

## 8. 성능 최적화

### 8.1 최적화 전략
- 계산 결과 캐싱
- 위젯 리빌드 최소화
- 메모리 사용 최적화

### 8.2 렌더링 최적화
- const 생성자 사용
- 불필요한 리빌드 방지
- 레이아웃 최적화 